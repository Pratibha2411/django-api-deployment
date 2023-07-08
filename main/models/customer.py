from django.db import models

class Customer(models.Model):
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    email=models.EmailField(max_length=20)
    phone=models.IntegerField()
    password=models.CharField(max_length=8)
    
    def register(self):
        self.save()
        
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    