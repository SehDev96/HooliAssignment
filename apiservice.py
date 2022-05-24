import requests as httprequest

API_URL = "http://demo1616407.mockable.io/v1/predict"


def get_prediction_reply(channel, message, restaurant_record, customer_record):
    parameters = {"channel": channel, "message": message, "restaurant_record": restaurant_record,
                  "customer_record": customer_record}
    response = httprequest.get(API_URL, params=parameters)
    return response
