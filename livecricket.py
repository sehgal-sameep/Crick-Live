
import requests
from datetime import datetime
class ScoreGet:
    def __init__(self):
        self.url_get_all_matches="https://api.cricapi.com/v1/currentMatches"
        self.apikey="7b040e2e-8704-4350-a5c9-490e6cf4a0df"

    def get_details(self):
        uri_params={"apikey":self.apikey}
        # resp=requests.get(self.url_get_all_matches,params=uri_params)
        resp=requests.get("https://api.cricapi.com/v1/currentMatches?apikey=7b040e2e-8704-4350-a5c9-490e6cf4a0df&offset=0")
        resp_dict=resp.json()


        data_found=0
        data="Here is the Live Score"
        for i in resp_dict['data']: 
            if(i['matchStarted']):
                todays_date=datetime.today().strftime('%Y-%m-%d')
                if(todays_date==i['date']):
                    if(i['venue']=="SCF Cricket Ground, Salem"):
                        data_found=1
                        if(data_found):
                            try:
                                data= "\n" + i['status'] + "\n"
                                match_score=i['score']
                                data+=str(match_score)
                            except KeyError as e:
                                print(e)
                        else:
                            data="No Live Match Going On"
                            break
        # print(match_score)
        return data

if __name__=="__main__":
    obj_score=ScoreGet()
    # obj_score.get_details()

    whatsapp_message=obj_score.get_details()

    from twilio.rest import Client
    a_sid="ACe4240d82a107d94ffcfc98fc0f55e604"
    auth_token="c4a69c8d1776582e35d9aa04c4437661"
    client=Client(a_sid,auth_token)
    message= client.messages.create(to='whatsapp:+919034826587', from_='whatsapp:+14155238886',body=whatsapp_message)
    print(message.sid)

print("\n")
print("Successfully Compiled")
print("\n")

