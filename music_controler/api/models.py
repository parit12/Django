from django.db import models
import string
import random
def generate_unique_code():
    lenght=6

    while True:
        code =''.join(random.choices(string.ascii_uppercase,k=lenght))
        if room.objects.filter(code=code).count() == 0:
            break
    
    return code

# Create your models here.
class room(models.Model):
    code =models.CharField(max_length=6,default=generate_unique_code,unique=True)
    host =models.CharField(max_length=50,unique=True)
    guest_can_pause =models.BooleanField(null=False,default=False)
    vote_to_skip =models.IntegerField(null=False,default=1)
    create_at =models.DateTimeField(auto_now_add=True)
