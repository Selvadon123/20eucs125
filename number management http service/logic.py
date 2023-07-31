from library.ServerAPI import ServerAPI
import validators

class Logic:
    def __init__(self):
        self.server_api = ServerAPI()
        
    def sorting_the_data(self, result: list):
        result = list(set(result))
        result.sort()
        
        return result

    def get_response(self, url_data):

        result = []
        for data in url_data:
            if validators.url(data):
                result = result + self.server_api.get_url_data(data)

            
            else:
                return {'code':404, 'message':'Invalid URL Passed'}
            
        result = self.sorting_the_data(result)
        return {'numbers':result}