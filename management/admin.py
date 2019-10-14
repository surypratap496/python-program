from django.contrib import admin
from .models import books, books_transactions
# Register your models here.


admin.site.register(books)
admin.site.register(books_transactions)
