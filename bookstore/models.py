from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=70, default="Anonymous", blank=False)
    last_name = models.CharField(max_length=70, default="Anonymous", blank=False)
    email = models.EmailField(max_length=70, default ="example@gmail.com", blank=False)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    verbose_name = "Author"
    verbose_name_plural = "Authors"

class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, default="book title", blank=False)
    image_cover = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="files", max_length=100)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title}"
