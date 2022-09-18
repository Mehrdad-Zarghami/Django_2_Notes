from django.db import models


class Note(models.Model):
    # A column (text) in our db that is of char(string) type with the max_length=100
    text = models.CharField(max_length=100)
    auther = models.CharField(max_length=50)

    def __str__(self):
        return str(self.auther) + '*' * 10
