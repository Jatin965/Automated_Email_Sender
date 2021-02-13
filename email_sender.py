import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jatin Saini'
email['to'] = 'mekusuri2000@gmail.com'
email['subject'] = 'Auto Generated Mail!!'

email.set_content(html.substitute({'name': 'Buddhu'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('02318002718@delhitechnicalcampus.ac.in', 'Prajat#494')
    smtp.send_message(email)
    print("All Done!!")