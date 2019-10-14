from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class books(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=50)
    book_isbn = models.IntegerField(primary_key=True)
    book_copys = models.IntegerField()

    def __str__(self):
        return self.book_title

class books_transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    issued_book = models.ForeignKey(books, on_delete=models.SET_NULL, null=True)
    issued_date = models.DateTimeField(auto_now = True)
    return_date = models.DateTimeField(auto_now = True)
    book_fine = models.IntegerField(blank=False)

    def __str__(self):
        return str (self.user)
