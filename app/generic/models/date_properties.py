from django.db import models


class DateProperties(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    date_altered = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
