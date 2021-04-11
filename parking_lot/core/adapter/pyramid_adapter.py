import json

from pyramid.response import Response


class PyramidAdapter:
    @staticmethod
    def handle_get(controller):
        def handle(code):
            response = controller(code)
            return Response(
                body=json.dumps({"code": response.code,
                                 "capacity": response.capacity,
                                 "open_hour": response.open_hour,
                                 "close_hour": response.close_hour,
                                 "occupied_spaces": response.occupied_spaces}),
                content_type='application/json',
                charset='utf-8')

        return handle
