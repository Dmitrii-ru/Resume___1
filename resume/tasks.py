from datetime import timedelta
from celery import shared_task
from django.utils import timezone

@shared_task
def send_email_task(massage_num, to_send, name, subject):
    from resume.python_prog.send_mail_prog import send_email_my
    try:
        send_email_my(massage_num, to_send, name, subject)
        return 'Your massage was send successfully!'
    except Exception as error:
        return f"{error} Error"


@shared_task
def check_email_old_task():
    from resume.models import EmailSend
    three_days_ago = timezone.now() - timedelta(days=3)
    old_mails = EmailSend.objects.filter(date__lt=three_days_ago)
    if old_mails:
        for obj in old_mails:
            massage = 2
            subject = 2
            send_email_task.delay(name=obj.name, massage_num=massage, to_send=obj.email, subject=subject)
        old_mails.delete()
