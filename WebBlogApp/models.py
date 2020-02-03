from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    badanBlog = models.TextField()

    def __str__(self):
        return self.judul