document.addEventListener('DOMContentLoaded', function() {
    // alert("script.js loaded successfully!");

    document.getElementById('send-emails-btn').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission

        extractEmailAddresses();
        extractEmailSubject();
        extractEmailBody();
    });
});

function extractEmailAddresses() {
    const targetEmails = document.getElementById('target-emails').value;
    console.log("Extracted Emails:", targetEmails);
}

function extractEmailSubject() {
    const emailSubject = document.getElementById('email-subject').value;
    console.log("Extracted Email Subject:", emailSubject);
}   

function extractEmailBody() {
    const emailBody = document.getElementById('email-body').value;
    console.log("Extracted Email Body:", emailBody);
}
