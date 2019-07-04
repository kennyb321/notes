# Text Messages with python

## Twilio
-Twilio account allows you to send and receive text messages and phone calls through your python application.

-Once youve signed up, use your **Account SID** and your **Auth Token**.

## REST API
-to send outgoing SMS message from twilio account, you need to make an **HTTP POST** to Twilio's **Message Resource**.

## Install Twilio
```pip install twilio```

## send message

-create file named send_sms.py
```
from twilio.rest import Client
account_sid = 'ACXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(body='this is the message that will be sent', from_='your phone number goes here',          from_='+15017122661',
         to='+15558675310'

print(message.sid)
```


## My Twilio Account info
email: kennyblanchard321@yahoo.com
PW: MadisonShannon1991!

trial#: 
+13214501680

account SID = ACd72f527e4e136bb350f5861ef6e6edb2
auth_token = 30b75e99795cf01eb06bb81a4c277993




## Install Flask and set up your development environment

-To receive and reply to SMS messages, we need to create a web application that can accept incoming requests.
-Well use **Flask**.

### Install pip and Virtualenv
-pip used to install Flask 
-virtualenv to create a unique sandbox for this project

```
pip install virtualenv
```

-use terminal to navigate to folder for your project, activate virtual environment.
```cd project_folder
virtualenv --no-site-packages .
```

**DONT FORGET THE PERIOD AT THE END OF PACKAGES**

-now activate virtual environment
``` source bin/activate ```

-youll know your in your virtual environment because in the name of your folder youll see your projectname in parentheses.



## Install dependancy's

-now we can install Flask. Create file called **requirments.txt** and add following lines of code.
``` Flask>=0.12
twilio~=6.0.0
```


```
source bin/activate
```





