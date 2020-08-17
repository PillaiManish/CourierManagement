from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courier_Details(models.Model):

    date_booked = models.DateTimeField(auto_now_add=True)

    from_name = models.CharField(max_length=50)
    from_address = models.TextField(null=True,blank=True)
    from_contact = models.IntegerField()
    
    
    to_name = models.CharField(max_length=50)
    to_address = models.TextField()
    to_contact = models.IntegerField()
    to_email = models.EmailField()

    parcel_weight = models.IntegerField(null=True,blank=True)

STATUS = (
    ('Received','Received'),
    ('Dispatched','Dispatched'),
    ('Deplayed','Deplayed'),
    ('Wrong Address','Wrong Address'),
    ('No one','No one'),
)


class Courier_Tracking(models.Model):
    courier_id = models.ForeignKey(Courier_Details,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(User,to_field='username')
    remarks = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=18, choices=STATUS)