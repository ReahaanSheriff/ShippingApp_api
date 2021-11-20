# from __future__ import print_function
# import time
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
# from pprint import pprint

from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

# Create your models here.
class CreateShipment(models.Model):
    orderId = models.CharField(max_length=25, primary_key=True)
    user_id_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add=True)
    pname = models.CharField(max_length=50)
    pmobile = models.IntegerField()
    paddress = models.CharField(max_length=100)
    ppincode = models.IntegerField()
    pcity = models.CharField(max_length=50)
    pstate = models.CharField(max_length=50)
    pcountry = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    dmobile = models.IntegerField()
    daddress = models.CharField(max_length=100)
    dcity = models.CharField(max_length=50)
    dstate = models.CharField(max_length=50)
    dpincode = models.IntegerField()
    dcountry = models.CharField(max_length=50)
    productName = models.CharField(max_length=50)
    productValue = models.IntegerField()
    weight = models.FloatField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    shippingPrice = models.IntegerField()
    estimateDate =  models.CharField(max_length=50)

class Tracking(models.Model):
    shipment = models.ForeignKey(CreateShipment, on_delete=models.CASCADE)
    pickScheduled = models.BooleanField(default = True)
    cancelled = models.BooleanField(default = False)
    outForPickup = models.BooleanField(default = False)
    pickedUp = models.BooleanField(default = False)
    transit = models.BooleanField(default = False)
    outForDelivery = models.BooleanField(default = False)
    delivered = models.BooleanField(default = False)




@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "Copy paste the token to reset your password \n {}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = 'api key'

#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
#     subject = "My Subject"
#     html_content = "<html><body><h1>"+email_plaintext_message +"</h1></body></html>"
#     sender = {"name":"John Doe","email":"reahaansheriff@gmail.com"}
#     to = [{"email":"reahaansherif@gmail.com","name":"Jane Doe"}]
# #cc = [{"email":"example2@example2.com","name":"Janice Doe"}]
# #bcc = [{"name":"John Doe","email":"example@example.com"}]
# #reply_to = {"email":"replyto@domain.com","name":"John Doe"}
#     headers = {"Some-Custom-Name":"unique-id-1234"}
#     params = {"parameter":"My param value","subject":"New Subject"}
#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)

#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         pprint(api_response)
#     except ApiException as e:
        #print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Swift shipping application"),
         # message:
         email_plaintext_message,
         # from:
         "reahaansheriff@gmail.com",
         # to:
         [reset_password_token.user.email],
     fail_silently=False,
     )