#python3

from twilio.rest import Client

def sms():
    #twilio Account SID and Auth Token
    client = Client("Account SID", "Auth Token")

    client.messages.create(to="+number",
                        from_="+number",
                        body="Hello from Python!")
    print("SMS send")
