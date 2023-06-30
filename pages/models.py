from django.db import models


class Pagestuff(models.Model):
    text = models.CharField(max_length=700, blank=False)
    path_to_file = models.ImageField(upload_to='images/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

