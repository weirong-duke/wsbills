import random

from django.db import models
from django.contrib.auth.models import User

from app.pools.models.pool import Pool

from app.words import generate_random_title_string

def generate_random_title():
    while True:
        generated_string = generate_random_title_string()
        if not(Pool.objects.filter(identifier=generated_string).exists()):
            return generated_string

class Transaction(models.Model):
    amount = models.FloatField()
    identifier = models.CharField(db_index=True, max_length=70, blank=True, null=True, default=generate_random_title, unique=True)
    notes = models.TextField(null=True, blank=True)
    pool =  models.ForeignKey(Pool, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1} - {2}'.format(self.user.first_name, self.user.last_name, self.notes)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = generate_random_title()

        super().save(*args, **kwargs)