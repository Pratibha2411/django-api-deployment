from rest_framework import serializers
from main.models.food_item import Food_item
from main.models.category import Category
from main.models.customer import Customer

class companyserializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Food_item
        fields='__all__'
        
        
class userserializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'        
        
          