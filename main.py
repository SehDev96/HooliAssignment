import sys

# flask
from flask import Flask, request, json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# models
from model.HooliRequestBody import HooliRequestBody
from model.Restaurant import Restaurant

# services
from databaseservice import get_restaurant_info_by_id, update_restaurant_info, get_customer_info_by_hooli_number, \
    get_restaurant_info_by_hooli_number
from apiservice import get_prediction_reply


app = Flask(__name__)

limiter = Limiter(app, key_func=get_remote_address)


@app.route("/")
def index():
    return "Hello World"


@app.route('/v1/hooli/message/', methods=['POST'])
@limiter.limit("1/second")  # maximum of 1 request per second
def message_hooli():
    """
    1. Make sure the content type and request body is valid
    2. Retrieve Customer Info from Database using sender number from request body
    4. Retrieve Restaurant Info from Database using receiver number from request body
    5. Make GET api call to http://demo1616407.mockable.io/v1/predict with
       request parameter:
       {
            "channel": "<RESTAURANT-ID>__<CUSTOMER-ID>",
            "message": request_body.message,
            "restaurant_record": <whole restaurant record from DB>, ==> encode this
            "customer_record": <whole customer record from DB> ==> encode
       }
    :return: reponse from http://demo1616407.mockable.io/v1/predict
    """
    if request.headers.get('Content-Type') == 'application/json':
        try:
            print(json.loads(request.data), file=sys.stderr)
            request_body = HooliRequestBody(json.loads(request.data))
            customer_data = get_customer_info_by_hooli_number(request_body.sender)
            restaurant_data = get_restaurant_info_by_hooli_number(request_body.receiver)
            channel = customer_data.get_id() + "_" + restaurant_data.get_id()
            message = request_body.message
            print("Before prediction", file=sys.stderr)
            api_prediction = get_prediction_reply(channel, message, restaurant_data, customer_data)
            print("After prediction", file=sys.stderr)
            if api_prediction.status_code == 200:
                return api_prediction.json(), api_prediction.status_code
            else:
                error = {"error": api_prediction.status_code, "error_message": "Error making api call"}
                return error, api_prediction.status_code

        # to handle incorrect api request body
        except KeyError as e:
            error_response = {"error": "Bad Request", "error_message": "{key} parameter not found!".format(key=e)}
            return error_response, 400

        except Exception:
            print(Exception.with_traceback(), file=sys.stderr)
            return "Internal Server Error", 500

    else:
        return 'Content-Type not supported'


@app.route('/v1/restaurant/<restaurant_id>', methods=["PUT"])
def update_restaurant(restaurant_id):
    """
    1. Get Restaurant Info from Database using restaurant id
    2. Update the details based on request body
    3. Update the Database with the new updated info

    :param restaurant_id:
    :return: basic http response ("202 OK")
    """
    try:
        request_body = json.loads(request.data)
        restaurant_details = Restaurant(None)
        restaurant_details.set_id(restaurant_id)
        restaurant_details.set_name(request_body["name"])
        restaurant_details.set_hooli_number(request_body["hooli_number"])

        print("Updating restaurant details...", file=sys.stderr)

        affected_rows = update_restaurant_info(restaurant_details)

        print("Done updating restaurant details.", file=sys.stderr)
        print("Affected rows: {row}".format(row=affected_rows), file=sys.stderr)

        if affected_rows > 0:
            return "202 OK", 202
        else:
            return "Internal Server Error", 500

    except KeyError as e:
        print("KeyError Exception!", file=sys.stderr)
        error_response = {"error": "Bad Request", "error_message": "{key} parameter not found!".format(key=e)}
        return error_response, 400

    except Exception:
        return "Internal Server Error", 500


@app.route('/v1/restaurant/<id>')
@limiter.limit("1/second")  # maximum of 1 request per second
def test_update_restaurant(id):
    """
    This function is to test the update restaurant endpoint.
    To check if the update was executed successfully

    :param id: restaurant_id
    :return: restaurant records
    """
    try:
        restaurant_data = get_restaurant_info_by_id(id)
        return restaurant_data.to_string(), 200

    except Exception:
        print(Exception.with_traceback(), file=sys.stderr)
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run()
