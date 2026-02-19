from flask import Flask, render_template, request, jsonify
from send_mail import send_email

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-emails', methods=['POST'])
def send_emails():
    if request.method == 'POST':
        data = request.get_json()
        recipient_emails = data.get('target_emails')  # This is a list
        subject = data.get('email_subject')
        message = data.get('email_body')
        
        # Convert list of emails to comma-separated string
        recipients_str = ','.join(recipient_emails) if isinstance(recipient_emails, list) else recipient_emails
        
        send_email(
            recipients=recipients_str,
            subject=subject, 
            message=message
        )

        print(f"Emails sent to: {recipients_str}")
        print(f"Subject: {subject}")
        print(f"Message length: {len(message)} chars")
        
        return jsonify({
            "status": "success",
            "recipient_count": len(recipient_emails),
            "subject": subject
        })

if __name__ == "__main__":
    app.run(debug=True)
