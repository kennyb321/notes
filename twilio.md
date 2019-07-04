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

-Then install both of these packages with pip in your terminal

```
bin/pip install -r requirments.txt
```

## Test Everything From Scratch
make sure your virtual environment is activated

```
cd projectFolder
source bin/activate 
```

-Then create a file named **run.py** and add following codes:
```
from flask import Flask
app = Flask(__name__)

@app.route("/sms")
def hello():
	return "Hello World!"

if __name == '__main__':
	app.run(debug=True)

```


Go to your terminal, and run your **run.py**.

you should see 
```
 * Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 619-824-977
```

now navigate to *http://localhost:5000/sms* and you should see "Hello World!" Message.

Now your ready to create our first Twilio messaging app!!


## Allow Twilio to talk to your Flask application
We are going to build a small Flask application to receive incoming messages. Before we do that, we need to make sure Twilio can reach your application.

Most Twilio services use **webhooks** to communicate with your applicatrion. When Twilio receivs and SMS, it reaches out to a URL in our Application for instructions on how to handle the message.

#### Webhooks
Webhooks allow you to build or set up integrations, such as Github Apps, which subscribe to certain events. When one of these events is triggered, well send an HTTP POST Payload to the webhooks URL.
   Webhooks can be used to update -an external issue tracker.


When working on your Flask Application in your development environment, your app is only available to the rest of your computer. We need to make it accessible over the internet.

There are a couple ways to do this, such as
*deploying application to Heroku
*or AWS

But we want somthing a little more lightweight to test Twilio.
We are going to use **Ngrok**. 
**ngrok** provides a unique URL on the **ngrok domain** which forwars incoming requests to your local development environment.

Download ngrok and extract the binary into your project folder.
run 
```
python run.py
```

open a new terminal and run:
```
./ngrok http 5000
```

## Receiving and replying to inbound sms messages with Flask

When somone sends a text message to our Twilio Phone number, Twilio Makes an HTP Request to your server asking for instructions on what to do next,
Once your received the request, you can tell Twilio to reply with an SMS kick off a phone call, sotre details about the SMS in your databasem or trigger somthing else. All up to you!

For this example, our flask app will reply to an incoming SMS message with a thank you to the sender, update our run.py file

```
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
	#respond to incoming messages with a friendly response
	resp = MessagingResponse()

	#add a message
	resp.message("Ahoy! Thanks so much for your message!")

	return str(resp)

if __name__ == '__main__':
	app.run(debug=True)
```

When your Twilio Phone Number receives an iincoming message, Twilio will send an HTTP request to your server.
save the file and restart the app. Double check that Ngrok is still running on your localhost port. Now Twilio can find your app. But first, **we need to tell Twilio where to look**.

## Configure your webhook URL

For Twilio to know where to look, you need to configure you Twilio phone number to call your webhook URL whenver a new message comes in.

1)Log into Twilio.com and go to the **Console's Numbers Page**
2)Click on your phone number.
3) Find the Messaging section. The default “CONFIGURE WITH” is what you’ll need: "Webhooks/TwiML".
4)n the “A MESSAGE COMES IN” section, select "Webhook" and paste in the URL you want to use. Make sure to add the /sms route to the end of your ngrok URL here:

## Test your application

If your localhost and NGrok Servers are up and running, werew ready for the fun part!!

Send a text message from your mobile phone. You should see a HTTP request in your Ngrok console. Your Flask app will proccess the text message, and youll get your response back as an SMS.



 # YEEEEES IT WOOOOOORRRKKKSS!!!!!!
Finnaly got it working.
ok, so basically it breaks down like this.
1)Buy a Twilio Account.
2)Save auth_token and account_sid
3)install twilio. We can now send text messages programatically with ouy python app. But we cannot receive messages. Right now our app can only talk to our local network. In order to connect it to the rest of the worl we need to set up a Flask web App.
4) Install and activate dev_env
	*pip install virtualenv
	*cd projectFolder
	*virtualenv --no-site-packages
	*SOURCE BIN/ACTIVATE
	*Youll know your virtualenv is active beacuse yioull see your path in parentheses.
5)Install Flask and dependancys
	*create text file named **requirements.txt** and add following code
		*Flask>=0.12
		*twilio~=6.0.0
6) install both packages and dependancys
	*bin/pip install -r requirements.txt
7) Download **ngrok**. Ngrok creates a unique url on the ngrok.io domain which forwards incoming requests to your local development env.
	*extract ngrok binary into our project folder.
8) Create file called **run.py** and add following code,
```
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
```
9)open terminal and run
``` 
python run.py
```.
10) in a seperate terminal, while **run.py** is still running, launch ngrok with following command:
```
./ngrok http 5000
```.

In the url after **forwarding**, copy the url.
11) Go to Twilio homepage -> **Console's Numbers Page**
	*Click on your phone number'
	*Find the messaging section where it says **A MESSAGE COMES IN**.
	*Paste the URL we copied from Ngrok, and add .sms to it.
	*it should look something like this,
	``` 
	 https://c886e0c1.ngrok.io/sms
	```.
12) Text your Twilio Phone number. The incoming text will register with your ngrok console as an incoming HTTP request. Your Flask app will proccess the request and respond with your defined function, which in this case texts bback with a message.


# run.py exaplained
This is the Flask app that responds to SMS Text messages on local Server and responds with a message of its own.
Code is as Follows
```
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
	#respond to incoming messages with a friendly response
	resp = MessagingResponse()

	#add a message
	resp.message("Ahoy! Thanks so much for your message!")

	return str(resp)

if __name__ == '__main__':
	app.run(debug=True)
```
.

#### app = Flask(__name__)

Create an instance of the Flask class for our app. 
If you are using a single module, you use __name__ because deponding on if its started as application or imported module the name will be different. This is needed so that Flask knows where to look for templates, static files, and so on.


#### @app.rout("/sms", methods=['GET', 'POST'])
#### def sms_ahoy_reply():
Define a function. @app.route('/sms') maps the function to the sms url. @route tells Flask what URL should trigger our function.


#### methods = ['GET', 'POST'])
**GET** - Sends data in unencrypted form to the server. Most common method.
**POST** - Used to send HTML form data to server. Data received by POST method is not cached by server.

#### resp = MessagingResponse
create an object of Messaging Response Class

#### resp.message("")
Create a message using message() function of MessaginResponse.





