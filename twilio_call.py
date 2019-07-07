from twilio.rest import Client

account_sid = 'ACd72f527e4e136bb350f5861ef6e6edb2'
auth_token = '30b75e99795cf01eb06bb81a4c277993'

client = Client(account_sid, auth_token)

call = client.calls.create(
		url='http://demo.twilio/com/docs/voice.xml',
		to='+13217206148',
		from_='+13214501680'
		)

print(call.sid)

