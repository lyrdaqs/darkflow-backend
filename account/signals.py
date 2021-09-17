from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from .tasks import send_email
from django.conf import settings



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}{}?token={}".format(settings.DOMAIN_NAME,
                                     reverse('account:password_reset_request'), reset_password_token.key)
    send_email.delay(
        "Password Reset for Darkflow",
        email_plaintext_message,
        "lyrdaq777@gmail.com",
        [reset_password_token.user.email]
    )


#/api/password_reset/confirm/  for confrim