from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    message = models.TextField()

    def __str__(self):
        return self.name