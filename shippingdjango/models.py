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

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Swift shipping application"),
        # message:
        email_plaintext_message,
        # from:
        "reahaansheriff@gmail.com",
        # to:
        [reset_password_token.user.email]
    )