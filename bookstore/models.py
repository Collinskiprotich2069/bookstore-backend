from django.db import models

class User(models.Model):
    pass


class Books(models.Model):
    title = models.CharField(max_length=70, default='book title', blank=False)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField( upload_to='files', max_length=100)
    class Meta:
        verbose_name = ('Book')
        verbose_name_plural = ('Books')
    def __str__(self):
        return  f'{self.title}'


