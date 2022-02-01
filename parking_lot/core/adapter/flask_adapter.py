class FlaskAdapter:
    @staticmethod
    def handle_get(controller):
        def handle(code):
            response = controller(code)
            return {"code": response.code,
                    "capacity": response.capacity,
                    "open_hour": response.open_hour,
                    "close_hour": response.close_hour,
                    "occupied_spaces": response.occupied_spaces}

        return handle
