from django.db import models
import string
import random

class URL(models.Model):
    # Fields for the original URL and the shortened code
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)

    # Custom save method to ensure a short code is generated if not provided
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self._create_unique_short_code()   # Generate short code if not already set
        super(URL, self).save(*args, **kwargs)

    # Method to create a unique 6-character short code
    def _create_unique_short_code(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choices(characters, k=6))
            if not URL.objects.filter(short_code=short_code).exists():
                break
        return short_code

    def __str__(self):
        # Return the original URL when the instance is represented as a string
        return self.original_url
