class HooliRequestBody:

    def __init__(self, request_body):
        self.sender = request_body["sender"]
        self.receiver = request_body["receiver"]
        self.message = request_body["message"]
