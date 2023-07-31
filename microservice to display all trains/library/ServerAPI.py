import requests as rq

class ServerAPI:
    
    def __init__(self):
        
        self.auth_url = "http://20.244.56.144/train/auth"
        self.client_scret = "JSsjvEbainjvEhwK" 
        
        self.get_trains_url = "http://20.244.56.144/train/trains"
        self.auth_token = self.get_auth_tokens()
    
    def get_auth_tokens(self):
        
        body = {
            "companyName": "Sri krishna College of Engineering and Technology",
            "clientID": "1d7d92bd-aa12-478b-b4fa-7283085c37ce",
            "ownerName": "Selvakumar S",
            "ownerEmail": "20eucs125@skcet.ac.in",
            "rollNo": "20eucs125",
            "clientSecret": "JSsjvEbainjvEhwK"
            
            }
        
        response = rq.post(self.auth_url, json=body)
        
        if response.status_code == 200:
            data = dict(response.json())
            return data['access_token']
        
        else:
            return 400
        
        
    def get_train_data(self, url):
        
        api_url = self.get_trains_url if url == 'all' else url
        if self.auth_token != 400:
            response = rq.get(api_url, headers={'Authorization': 'Bearer '+self.auth_token})
            
            if response.status_code == 200:
                data = list(response.json())
                return data
            
            else:
                return 400
            
            
        else:
            return 400
        
        


    