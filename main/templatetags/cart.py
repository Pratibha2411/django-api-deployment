from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(food,cart):
    keys=cart.keys()
    for i in keys:
        # print(i)
        if int(i)==food.id:
            return True;
    # print(type(i),type(food.id))    
    print(keys)
    print(food,cart)
    return False;
