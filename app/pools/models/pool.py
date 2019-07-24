import random

from django.db import models

from app.words import generate_random_title_string

def generate_random_title():
    while True:
        generated_string = generate_random_title_string()
        if not(Pool.objects.filter(identifier=generated_string).exists()):
            return generated_string

class Pool(models.Model):
    name = models.CharField(blank=True, max_length=250)
    description = models.TextField()
    identifier = models.CharField(db_index=True, max_length=70, blank=True, null=True, default=generate_random_title, unique=True)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.identifier)

    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = generate_random_title()

        super().save(*args, **kwargs)

