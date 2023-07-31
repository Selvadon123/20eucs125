from library.ServerAPI import ServerAPI

class Logic:
    def __init__(self):
        self.server_api = ServerAPI()
        
    def get_all_trains(self):
        return self.server_api. get_train_data(url='all')