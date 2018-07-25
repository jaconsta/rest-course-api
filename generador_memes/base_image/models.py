from django.db import models


class Image(models.Model):
    # File descriptors
    name = models.CharField(max_length=150)
    file = models.ImageField(upload_to='static/uploads/base_for_memes')

    # Update information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
