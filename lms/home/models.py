from django.db import models

class App(models.Model):
    app_name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.app_name