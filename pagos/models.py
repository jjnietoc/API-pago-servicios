from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Pagos(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    monto = models.FloatField(default=0.0)


class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    logo = models.ImageField()

class PaymentUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_user')
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services')
    amount = models.IntegerField()
    payment_date = models.DateField(auto_now_add=False)
    expiration_date = models.DateField()

class ExpiredPayments(models.Model):
    payment_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exp_payment_user')
    penalty_fee_amount = models.IntegerField()