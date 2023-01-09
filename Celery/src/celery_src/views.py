from django.views.generic import CreateView
from celery_src.forms import ContactForm
from celery_src.models import Contact
from celery_src.service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/' #переход на главную страницу
    template_name = 'celery_src/contact.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email) #отправка сообщения,  пока не выполнеться дальше не пойдет
        send_spam_email.delay(form.instance.email) # подключаю вполнение функции через celery delay() таска будет обрабатывать параллено
        return super().form_valid(form)

    #celery -A src worker --loglevel=INFO
# , запускается тамже где manage.py запуск воркера

