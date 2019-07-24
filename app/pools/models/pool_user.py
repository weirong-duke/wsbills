from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from app.pools.models.pool import Pool

class PoolUser(models.Model):
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    unverified_email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        default_related_name = 'pool_users'

    def validate_unique(self, exclude=None):
        if self.user:
            email = self.user.email
        else:
            email = self.unverified_email

        if PoolUser.objects.filter(Q(unverified_email=email) | Q(user__email=email), pool=self.pool).exists():
            raise ValidationError("This email already exists in this pool")

    def __str__(self):
        return '{0} - {1}'.format(self.pool, self.user or self.unverified_email)