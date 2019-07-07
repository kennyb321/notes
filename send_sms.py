from twilio.rest import Client
account_sid = 'ACd72f527e4e136bb350f5861ef6e6edb2'
auth_token = '30b75e99795cf01eb06bb81a4c277993'
my_number = '13214501680'

client = Client(account_sid, auth_token)
message = client.messages.create(to="+13217206148", 
				from_=my_number,
				body="Testing")

print(message.sid)
