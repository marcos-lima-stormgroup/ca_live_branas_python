import json

from chalice import Response


class ChaliceAdapter:
    @staticmethod
    def handle_get(controller):
        def handle(code) -> Response:
            response = controller(code)
            return Response(
                body=json.dumps({"code": response.code,
                                 "capacity": response.capacity,
                                 "open_hour": response.open_hour,
                                 "close_hour": response.close_hour,
                                 "occupied_spaces": response.occupied_spaces}),
                status_code=200)

        return handle
