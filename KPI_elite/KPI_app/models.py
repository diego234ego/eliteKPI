from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Collaborator(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    comment = models.TextField(blank=True)

class KPI(models.Model):
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name='kpis')
    title = models.CharField(max_length=100)


class DailyResult(models.Model):
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    value = models.FloatField()
    class Meta: 
        db_table="facturas"