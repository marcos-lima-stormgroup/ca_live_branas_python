class BottleAdapter:
    @staticmethod
    def handle_get(controller):
        def handle(code):
            response = controller(code)
            return response
        return handle
