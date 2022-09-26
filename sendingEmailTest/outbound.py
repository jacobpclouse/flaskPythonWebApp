# Source: https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python
# mailgun api: https://www.mailgun.com/

# https://stackoverflow.com/questions/33313858/importerror-no-module-named-email-mime-email-is-not-a-package
# https://bobbyhadz.com/blog/python-attributeerror-bytes-object-has-no-attribute-encode

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

me = "email here"
you = "YOU WISH email"
textfile = "sample.txt"

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open(textfile, 'rb') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# msg = msg.encode('utf-8')

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()