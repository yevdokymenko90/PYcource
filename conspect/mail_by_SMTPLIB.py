"""mail by SMTPLIB"""

from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())  # Add parentheses after read_text
html_content = html_template.substitute({'name': 'Dmytro', 'date':'tomorrow'})  # Add colon after html_template.substitute()

my_email['From'] = 'Dmytro <90evdokimenko@gmail.com>'
my_email['to'] =   'test@gmail.com'
my_email['subject'] = 'WTF!'
my_email.set_content(html_content, 'html')

with open('images/giphy.gif', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='gif', filename='giphy.gif')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    #smtp_server.starttls()
    #smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('email sent successfully')
    
