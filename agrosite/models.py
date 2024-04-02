from django.db import models

class Category(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.id}'