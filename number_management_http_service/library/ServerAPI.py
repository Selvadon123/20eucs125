import requests as rq

class ServerAPI:
            
    def get_url_data(self, url):
        

            response = rq.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data['numbers']
            
            else:
                return 400
            

        
        


    