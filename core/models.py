from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    title = models.TextField()
    author = models.CharField(max_length=255)
    body = models.TextField()
    polarity = models.FloatField()

    class Meta:
        db_table = 'uganda'
        managed = False
