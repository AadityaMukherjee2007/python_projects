from flask import Flask, render_template
from send_mail import send_email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-emails', methods=['POST'])
def send_emails():
    # Here you would extract email data from the request and call send_email
    # For demonstration, we'll use placeholder values

if __name__ == "__main__":
    app.run(debug=True)
