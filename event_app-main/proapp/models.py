from django.db import models

class Event(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booinkg_date=models.DateField()
    booinkg_on=models.DateField(auto_now=True)    
