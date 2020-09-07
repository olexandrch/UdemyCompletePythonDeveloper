#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 217. Sending Emails With Python

# https://docs.python.org/3/library/email.examples.html
# https://docs.python.org/3/library/email.html#module-email
# https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/



import smtplib
from email.message import EmailMessage
import time

# Ask for Gmail email address and password. It will send 'from' and 'to' the same address
# Add app password in gmail settings and use it.
email_address = input('Provide Gmail email address: ')
email_password = input('Provide password for Gmail email address: ')

email_name = email_address[0:email_address.find('@')]

email = EmailMessage()
email['from'] = email_name
email['to'] = email_address
email['subject'] = 'test'

localtime = time.asctime( time.localtime(time.time()) )
email_content = f"""Hi There!
Now is {localtime}"""

email.set_content(email_content)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    print('All Good!')

