from django.contrib import admin

# Register your models here.
from .models.pool import Pool
from .models.pool_user import PoolUser

admin.site.register(Pool)
admin.site.register(PoolUser)