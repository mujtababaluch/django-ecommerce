from django.conf import settings
from django.core.mail import send_mail




def send_account_activation_email(email , email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject , message , "saadsheikh131959@gmail.com" , [email])

    # email_from
# s = send_mail("subject","message content 2","saadsheikh131959@gmail.com", ["abdbasitali313595@gmail.com"])
