class SwapiPeopleSorterView:
    @staticmethod
    def format_response(data):
        if isinstance(data, list):
            return {"status": "success", "data": data}, 200
        return {"status": "error", "message": "Failed to retrieve data"}, 500
