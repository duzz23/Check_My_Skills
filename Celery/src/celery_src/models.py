from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=30)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



