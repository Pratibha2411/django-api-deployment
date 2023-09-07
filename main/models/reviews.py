from django.db import models

class Review(models.Model):
    review=models.TextField(max_length=1000)
    
    
    def re(self):
        return Review.objects.all()
        
        
    
    