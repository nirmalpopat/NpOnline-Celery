
# from celery.utils.log import get_task_logger
# from celery.decorators import task
# from celery import task
from django.core.mail import send_mail
from celery import shared_task
# from feedback.emails import send_feedback_email

# logger = get_task_logger(__name__)


@shared_task(bind=True)
def fun(self, name, subject, message):
    send_mail(
        subject,
        message,
        'popatnirmal2233@gmail.com',
        ['popatnirmal2233@gmail.com', 'tejalpopat735@gmail.com', 'harshmangvani89@gmail.com'],
        fail_silently=False,
    )
    return 'Done'