from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'тиби спам',
        'это будет больно',
        'duzz@mail.ru',
        [user_email],
        fail_silently=False,
    )
