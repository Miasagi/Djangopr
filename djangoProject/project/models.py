from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title




