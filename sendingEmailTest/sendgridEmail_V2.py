## https://docs.sendgrid.com/for-developers/sending-email/quickstart-python#complete-code-block
# https://stackoverflow.com/questions/39717986/httperror-http-error-401-unauthorized-for-sendgrid-integration-with-python

# importing library
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


# # getting the api key read into the file 
# api_key = open("apiKey.txt", "r")
# print(api_key.read())



# sending email
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
#sg = sendgrid.SendGridAPIClient(api_key)
from_email = Email("mp3converterandencryptor@gmail.com")  # Change to your verified sender
to_email = To("notmyrealemailduh@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)
