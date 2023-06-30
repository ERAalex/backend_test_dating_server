from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

# запуск worker ов: celery -A core.celery worker


@shared_task
def confirmation_relation_email_celery(user_email, user_name, user_match_email):
    """Отправляем сообщение при подтверждении заказа - Клиенту"""

    message = f'Вы понравились {user_name}!, почта участника: {user_email}.\n'
    recipient_list = [user_match_email]
    send_mail(subject='У Вас взаимная связь!', message=message, from_email=settings.EMAIL_HOST_USER,
              recipient_list=recipient_list)
