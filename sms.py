#python3

from twilio.rest import Client

def sms():
    #twilio Account SID and Auth Token
    client = Client("Account SID", "Auth Token")

    client.messages.create(to="+number",
                        from_="+number",
                        body="Check the Tournament http://en.intelextrememasters.com/season-12/oakland/pubg/")
    print("SMS send")
