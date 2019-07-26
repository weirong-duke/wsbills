from django.db import models

from app.generic.models.date_properties import DateProperties
from app.pools.models.pool import Pool
from app.pools.models.pool_user import PoolUser

from app.words import generate_random_identifier_string

def generate_random_identifier():
    while True:
        generated_string = generate_random_identifier_string()
        if not(Pool.objects.filter(identifier=generated_string).exists()):
            return generated_string

class Transaction(DateProperties):
    amount = models.FloatField()
    identifier = models.CharField(db_index=True, max_length=70, blank=True, null=True, default=generate_random_identifier, unique=True)
    notes = models.TextField(null=True, blank=True)
    pool =  models.ForeignKey(Pool, on_delete=models.CASCADE)
    title = models.CharField(max_length=70, blank=True, null=True)
    pool_user = models.ForeignKey(PoolUser, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.pool_user:
            if self.pool_user.user:
                return '{0} {1} - {2}'.format(self.pool_user.user.first_name, self.pool_user.user.last_name, self.title)
            return '{0} - {1}'.format(self.pool_user.unverified_email, self.title)
        return 'Removed User - {0}'.format(self.title)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = generate_random_identifier()

        super().save(*args, **kwargs)