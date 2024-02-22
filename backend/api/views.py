from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from products.models import Product 
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request):
    """ 
    DRF API VIEWS
    """
  
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:    
    #     '''     
    #     Serialization:
    #         Taking model instance and converting it to dictionary 
    #         and returning it as a Json response to Python Client.
    #     '''
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price

    #     # data = model_to_dict(model_data,fields=['id','title','content','price','sales_price'])
    #     # print(instance.id)
    #     data = ProductSerializer(instance).data
    
    ''' 
    Validating the data using serializers 

    '''
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response(serializer.errors)

