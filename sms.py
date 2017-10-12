#python3

from twilio.rest import Client

def sms():
    #twilio Account SID and Auth Token
    client = Client("ACf24b3bdc844d344e78195d568f618f2b", "37ba6ef47864fe8f7c5bd6ed12b9172d")

    client.messages.create(to="+number",
                        from_="+number",
                        body="Hello from Python!")
    print("SMS send")
