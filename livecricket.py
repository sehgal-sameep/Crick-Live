
import requests
from datetime import datetime
class ScoreGet:
    def __init__(self):
        self.url_get_all_matches="https://api.cricapi.com/v1/currentMatches"
        self.apikey="YOUR API KEY"

    def get_details(self):
        uri_params={"apikey":self.apikey}
        # resp=requests.get(self.url_get_all_matches,params=uri_params)
        resp=requests.get("https://api.cricapi.com/v1/currentMatches?apikey=YOUR_API_KEY&offset=0")
        resp_dict=resp.json()


        data_found=0
        data="Here is the Live Score"
        for i in resp_dict['data']: 
            if(i['matchStarted']):
                todays_date=datetime.today().strftime('%Y-%m-%d')
                if(todays_date==i['date']):
                    if(i['venue']=="STADIUM_NAME"):
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
    a_sid="Twilio_A_SID"
    auth_token="Twilio_Auth_Token"
    client=Client(a_sid,auth_token)
    message= client.messages.create(to='whatsapp:+91CONTACT_No', from_='whatsapp:+14155238886',body=whatsapp_message)
    print(message.sid)

print("\n")
print("Successfully Compiled")
print("\n")

