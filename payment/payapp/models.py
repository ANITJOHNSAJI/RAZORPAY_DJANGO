from django.db import models
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from . constants import PaymentStatus

# Create your models here.
class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254,blank=False,null=False)
    amount = models.FloatField(_("Amount"),blank=False,null=False)
    status=CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False
    )
    provider_order_id=models.CharField(
        _("Order ID"),max_length=40,null=False,blank=False
    )
    payment_id=models.CharField(
        _("Payment ID"),max_length=36,null=False,blank=False
    )
    signature_id=models.CharField(
        _("Signature ID"),max_length=128,null=False,blank=False
    )

    def __str__(self):
        return f"{self.id}{self.name}{self.status}"
    
