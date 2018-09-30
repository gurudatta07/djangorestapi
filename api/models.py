from django.db import models

class Dataset1(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)
