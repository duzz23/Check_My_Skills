from django.core.mail import send_mail
from src.celery import app
from .models import Contact
from .service import send


#Создаю задачи для celery
@app.task # этот декоратор говорит что это Таска
def send_spam_email(user_email):
    send(user_email)

# celery -A src worker --loglevel=INFO команда запуска таски


@app.task # этот декоратор говорит что это Таска
def send_beat_email():
    for contacts in Contact.objects.all():
        send_mail(
            "Вы подписались на рассылку",
            "это письмо будет приходить каждые 1 минy",
            "duzz@mail.ru",
            [contacts.email],
            fail_silently=False,
        )
# celery -A src beat --loglevel=INFO запуск новой такски с повторение выполнени первой "beat" заместо "woker"

@app.task
def add(x, y):
    return x + y
# выполнение команды через python manage.pe shell
# >>> from celery_src.tasks import add
# >>> add.delay(4,8)


# Повторять задачу если она не выполнелась, пока не выполниться. "retry"
# default_retry_dalay=5*60 настройка повторения таски каждые 3 мин
@app.task(bind=True, default_retry_dalay=5*60)
def my_task_retry(self, a, b):
    #Цикл будет повторяться пока не выполниться.
    try:
        return a + b
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
    #countdown=60 отложеность задачи
    #retry метод повтора
