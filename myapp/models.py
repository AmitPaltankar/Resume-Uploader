from django.db import models

State_choice =(('karnataka','karnataka'),
('punjab','punjab')
)
gender_choice=(('male','male'),('female','female'),('undifind','undifind'))


class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender= models.CharField(choices=gender_choice,max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=State_choice ,max_length=100)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profileimg',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)



# Create your models here.
