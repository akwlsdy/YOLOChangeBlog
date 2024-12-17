from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        app_label = 'servicesystem'

    def __str__(self):
        return self.title
