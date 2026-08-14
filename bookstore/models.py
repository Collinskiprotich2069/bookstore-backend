from django.db import models



class Books(models.Model):
    title = models.CharField(max_length=70, default='book title', blank=False)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ('Book')
        verbose_name_plural = ('Books')
    def __str__(self):
        return  f'{self.title}'


