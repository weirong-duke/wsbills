from django.db import models
from django.contrib.auth.models import User

from app.words import generate_random_title
from app.pools.models.pool import Pool

class Transaction(models.Model):
    amount = models.FloatField()
    pool =  models.ForeignKey(Pool, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    identifier = models.CharField(max_length=50, blank=True, null=True, default=generate_random_title, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} - {2}'.format(self.user.first_name, self.user.last_name, self.notes)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = generate_random_title()

        super().save(*args, **kwargs)