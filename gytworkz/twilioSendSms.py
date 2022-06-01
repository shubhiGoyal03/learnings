# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC247306a596c31ce4fd78f7704c2f7811'
auth_token = 'c32f4f51111d5898d715e01ea7c90458'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='This will be the body of the new message!',
                              from_='+19705985357',
                              to='+919783947656'
                          )

print(message.sid)
