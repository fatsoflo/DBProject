from django.db import models

# from industry.models import Industry

# Create your models here.
# Companies (companyId, industryId, companyName, companyAddress)
class Company(models.Model):
    industry = models.ForeignKey(
        'industry.Industry',
        on_delete=models.CASCADE,
        blank=True,)
    company_name = models.CharField(max_length=30)
    company_address = models.CharField(max_length=200)