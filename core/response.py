from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, msg):
        super().__init__(data={"message": msg})
