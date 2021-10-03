from django.db import models
from pytz import unicode


class Post(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)
    author_name = models.CharField(max_length=30)
    # я решила, что имя автора - это текст, потому что имя,
    # если бы был просто автор, то это был бы уже ForeignKey

    def __str__(self):
        return unicode(str(self.title))
