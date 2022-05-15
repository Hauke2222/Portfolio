from django.db import models

# Create your models here.


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    # user_id =

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)

    def __str__(self):
        return self.comment
