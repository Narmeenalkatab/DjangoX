from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Snack(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField()
    purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='snacks')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('snack_list')
