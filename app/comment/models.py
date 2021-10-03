from django.db import models
from pytz import unicode


class Comment(models.Model):
    author_name = models.CharField(max_length=30)
    # аналогично и в этой модели с именем, хотя может вы имели в
    # виду отношение к полю имя?
    content = models.TextField()
    creation_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return unicode(str(self.content))
