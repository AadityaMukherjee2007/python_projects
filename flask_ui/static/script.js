document.addEventListener('DOMContentLoaded', function() {
    // alert("script.js loaded successfully!");

    document.getElementById('send-emails-btn').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission

        extractEmailData();
    });
});

function extractEmailData() {
    const targetEmails = document.getElementById('target-emails').value;
    const emailSubject = document.getElementById('email-subject').value;
    const emailBody = document.getElementById('email-body').value;

    console.log("Extracted Emails:", targetEmails);
    console.log("Extracted Email Subject:", emailSubject);
    console.log("Extracted Email Body:", emailBody);

    fetch('/send_emails', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            target_emails: targetEmails,
            email_subject: emailSubject,
            email_body: emailBody
        })
    }   ).then(response => response.json())
      .then(data => {
          console.log('Success:', data);
          alert('Emails sent successfully!');
      })
      .catch((error) => {
          console.error('Error:', error);
          alert('Error sending emails.');
      });
}