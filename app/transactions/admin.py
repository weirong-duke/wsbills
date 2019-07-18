from django.contrib import admin

# Register your models here.
from .models.transaction import Transaction

admin.site.register(Transaction)