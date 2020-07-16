import smtplib
from email.message import EmailMessage
email =EmailMessage()
email['from'] ='Santhi Priya'
email['to'] ='sivasankar.ch15@gmail.com'
email['subject'] ='test mail for Python'
email.set_content('Hey Pig,'
                  'Python Programmer Loves you a lot')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('santhipriya13@gmail.com','Harinichoti@2')
    smtp.send_message(email)
    print('sent mail')