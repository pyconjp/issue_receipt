from django.db import models

class Attendee(models.Model):
    register_id = models.CharField(max_length=10)
    register_type = models.CharField(max_length=8)

    def __str__(self):
        return self.register_id
