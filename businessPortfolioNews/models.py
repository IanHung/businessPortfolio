from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    pubdate = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    link = models.URLField(blank = True)
    def __str__(self):
        return self.title