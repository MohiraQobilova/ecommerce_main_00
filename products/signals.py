from http.client import responses

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from pycparser.ply.yacc import token
from pyexpat.errors import messages
from urllib3 import request

from .tasks import send_telegram_notification
from .models import Order


@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:
        token = settings.TELEGRAM_BOT_TOKEN
        method = 'sendMessage'

        message_text = f"New Oreder: {instance.id}\n Product {instance.product.name}\n Quantity: {instance.quantity}"
                       f"Client: {instance.customer.username}\n tel: {instance.phone_number}"



        response = requests.post(
            url=f'https://api.telegram.org/bot{token}/{method}',
            data={'chat_id':,'text':message_text}

        ).json()











    # if created:  # Check if a new record is created
    #     send_telegram_notification.delay(
    #         order_id=instance.id,
    #         product_name=instance.product.name,
    #         quantity=instance.quantity,
    #         customer_username=instance.customer.username,
    #         phone_number=instance.phone_number
    #     )
