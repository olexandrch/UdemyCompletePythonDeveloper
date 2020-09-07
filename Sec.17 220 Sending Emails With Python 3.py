#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 217. Sending Emails With Python

# https://docs.python.org/3/library/email.examples.html
# https://docs.python.org/3/library/email.html#module-email
# https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
# https://docs.python.org/3/library/string.html#template-strings


import smtplib
from email.message import EmailMessage
import time
from string import Template
from pathlib import Path

html = Template(Path('Sec.17 220 Sending Emails With Python 3.html').read_text())

# Ask for Gmail email address and password. It will send 'from' and 'to' the same address
# Add app password in gmail settings and use it.
email_address = input('Provide Gmail email address: ')
email_password = input('Provide password for Gmail email address: ')

email_name = email_address[0:email_address.find('@')].capitalize()

email = EmailMessage()
email['from'] = email_name
email['to'] = email_address
email['subject'] = 'test'

localtime = time.asctime( time.localtime(time.time()) )

email.set_content(html.substitute({'name': email_name, 'amount': '$1,000,000', 'now': localtime}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    print('All Good!')

