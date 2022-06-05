from django.db import models

# Create your models here.
class Project(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    source_code = models.CharField(max_length=250, blank=True)
    project_url = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

    def full_author_name(self):
        return self.author.get_full_name()
