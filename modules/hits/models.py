from tabnanny import verbose
from django.db import models
from modules.hitman.models import Hitmen

# Create your models here.
class Hits(models.Model):
    STATUS_HITS_CHOICES = (
        ("ASSIGNED", "ASSIGNED"),
        ("Failed", "Failed"),
        ("Completed", "Completed")
    )
    
    assignee = models.IntegerField(null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    target = models.CharField(max_length=250, null=False, blank=False)
    status = models.CharField(choices=STATUS_HITS_CHOICES, 
                              null=False, blank=False, max_length=9)
    created_by = models.ForeignKey(Hitmen, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Hits'