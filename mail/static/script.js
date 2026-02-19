document.addEventListener('DOMContentLoaded', function() {
    const chipsContainer = document.getElementById('target-emails-container');
    const input = document.getElementById('target-emails-input');
    let emails = [];

    function renderChips() {
        chipsContainer.innerHTML = '';
        emails.forEach((email, idx) => {
            const chip = document.createElement('span');
            chip.className = 'inline-flex items-center bg-gradient-to-r from-blue-600 to-blue-500 hover:from-blue-700 hover:to-blue-600 text-white rounded-full px-3 py-1 text-xs font-medium shadow-md hover:shadow-lg transition-all duration-200';
            chip.textContent = email;

            const remove = document.createElement('button');
            remove.type = 'button';
            remove.className = 'ml-2 text-white hover:text-blue-100 font-bold text-base leading-none hover:scale-110 transition-transform';
            remove.innerHTML = '×';
            remove.addEventListener('click', (e) => {
                e.preventDefault();
                emails.splice(idx, 1);
                renderChips();
            });

            chip.appendChild(remove);
            chipsContainer.appendChild(chip);
        });
    }

    function validateEmail(email) {
        return /\S+@\S+\.\S+/.test(email);
    }

    function addEmailsFromString(str) {
        const parts = str.split(/[,\s]+/).map(s => s.trim()).filter(Boolean);
        parts.forEach(p => {
            if (validateEmail(p) && !emails.includes(p)) {
                emails.push(p);
            }
        });
        renderChips();
    }

    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ',') {
            e.preventDefault();
            const val = input.value.trim();
            if (val) {
                addEmailsFromString(val);
                input.value = '';
                input.focus();
            }
        } else if (e.key === 'Backspace' && input.value === '') {
            e.preventDefault();
            emails.pop();
            renderChips();
        }
    });

    input.focus();

    document.getElementById('send-emails-btn').addEventListener('click', function(event) {
        event.preventDefault();
        if (input.value.trim()) {
            addEmailsFromString(input.value.trim());
            input.value = '';
        }
        if (emails.length === 0) {
            alert('Please add at least one email address');
            return;
        }
        extractEmailData();
    });

    function extractEmailData() {
        // Build a list of emails from the `emails` array (single source of truth)
        const targetEmailsList = emails.slice();
        const emailSubject = document.getElementById('email-subject').value;
        const emailBody = document.getElementById('email-body').value;

        console.log("Extracted Emails:", targetEmailsList);
        console.log("Extracted Email Subject:", emailSubject);
        console.log("Extracted Email Body:", emailBody);

        fetch('/send-emails', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                target_emails: targetEmailsList,
                email_subject: emailSubject,
                email_body: emailBody
            })
        }).then(response => response.json())
          .then(data => {
              console.log('Success:', data);
              alert('Emails sent successfully!');
          })
          .catch((error) => {
              console.error('Error:', error);
              alert('Error sending emails.');
          });
    }
});