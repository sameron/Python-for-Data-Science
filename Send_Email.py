
"""
Send an email to a specified recipient:
"""

import smtplib

# Set the email server and login credentials
server = smtplib.SMTP('smtp.example.com')
server.login('username', 'password')

# Set the sender and recipient email addresses
sender = 'sender@example.com'
recipient = 'recipient@example.com'

# Set the subject and body of the email
subject = 'Test Email'
body = 'This is a test email sent using Python.'

# Format the email as an MIME message
message = f'Subject: {subject}\n\n{body}'

# Send the email
server.sendmail(sender, recipient, message)

# Disconnect from the server
server.quit()