from django.db import models

from app.words import generate_random_title

class Pool(models.Model):
    name = models.CharField(blank=True, max_length=250)
    description = models.TextField()
    identifier = models.CharField(max_length=50, blank=True, null=True, default=generate_random_title, unique=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.identifier)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = generate_random_title()

        super().save(*args, **kwargs)