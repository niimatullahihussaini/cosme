from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
import time
from .models import Order

from django.conf import settings

@receiver(valid_ipn_received)
def paypa_payment_received(sender, **kwargs):
    time.sleep(10)

    # Grab the infor that paypal
    paypal_obj = sender

    my_Invoice = str(paypal_obj.invoice)


    my_Order = Order.objects.get(invoice=my_Invoice)
    # print(paypal_obj)
    # print(f'Amount Paid{paypal_obj.mc_gross}')
    my_Order = True
    my_Order.save()