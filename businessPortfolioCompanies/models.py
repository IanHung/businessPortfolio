from django.db import models

# Create your models here.
class Company(models.Model):
    img = models.ImageField(upload_to='images/businessPortfolioCompanies/')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    webaddress = models.URLField(blank=True)
    contact = models.CharField(max_length=200)
    dateFounded = models.DateTimeField('date founded')
    success = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Companies'