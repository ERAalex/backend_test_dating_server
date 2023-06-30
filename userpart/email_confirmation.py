from django.conf import settings
from django.core.mail import send_mail


def confirmation_relation_email(user_email, user_name, user_match_email):

    message = f'Вы понравились {user_name}!, почта участника: {user_email}.\n'
    recipient_list = [user_match_email]
    send_mail(subject='У Вас взаимная связь!', message=message, from_email=settings.EMAIL_HOST_USER,
              recipient_list=recipient_list)
