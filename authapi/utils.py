#this class is for 	sending email using django's email message
import os
from django.core.mail import EmailMessage

class Util:
	@staticmethod
	def send_email(data):
		email = EmailMessage(
				subject = data['subject'],
				body = data['body'],
				from_email = os.environ.get('EMAIl_FROM'),
				to = [data['to_email']]
			)
		email.send()





