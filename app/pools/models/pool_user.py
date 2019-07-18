from django.db import models
from django.contrib.auth.models import User

from app.pools.models.pool import Pool

class PoolUser(models.Model):
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('pool', 'user')

    def __str__(self):
        return '{0} - {1}'.format(self.pool, self.user)