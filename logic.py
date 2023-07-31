from library.ServerAPI import ServerAPI
from collections import OrderedDict

class Logic:
    def __init__(self):
        self.server_api = ServerAPI()
        
    def sorting_the_data(self, data):
        """
            30min departure time ignored
            ascending order of price
            descending order of tickes
            descending order of departure time
        """
        temp = []
        
        for ele in data:
            
            if len(temp) == 0:
                temp.append(ele)
                
            else:
                prev_ele = temp[len(temp)-1]
                
                # checking departure
                hrs, mins, sec = (ele['departureTime'].get('Hours'), ele['departureTime'].get('Minutes'), ele['departureTime'].get('Seconds'))
                prv_hrs, prv_mins, prv_sec = hrs, mins, sec = (prev_ele['departureTime'].get('Hours'), prev_ele['departureTime'].get('Minutes'), prev_ele['departureTime'].get('Seconds'))
                
                if hrs == 0:
                    if mins <= 30:
                        continue
                    
                # ascending order of price
                if ele['price']['sleeper'] + ele['price']['AC'] > prev_ele['price']['sleeper'] + prev_ele['price']['AC']:
                    # descending order of total tickets available
                    if ele['seatsAvailable']['sleeper'] + ele['seatsAvailable']['AC'] < prev_ele['seatsAvailable']['sleeper'] + prev_ele['seatsAvailable']['AC']:
                        # descending order of depature time
                        current_depart_time = hrs*60*60 + mins * 60 + sec
                        prv_depart_time = prv_hrs*60*60 + prv_mins * 60 + prv_sec
                        
                        if  current_depart_time < prv_depart_time:
                            temp.append(ele)
                            continue
                        
                        
                temp.insert(len(temp)-2, ele)
                
        return temp        


    def get_all_trains(self):

        result = self.server_api.get_train_data(url='all')
        result = self.sorting_the_data(result)

        return result