from django.shortcuts import render
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from PIL import Image
from .utils import image_prediction

# Create your views here.
class PredictDigits(APIView):
    parser_classes = [MultiPartParser]
    def post(self , request):
        try:
    
            image_file = request.FILES['image']
            image = Image.open(image_file).convert('L') # converts the image into grayscale
            image = image.resize((28,28)) # resize the image that the model expects
            image_array = np.array(image)/255.0
            predict_digit = image_prediction(image)
            return Response({'prediction':int(predict_digit)})
        except Exception as e:
            return Response({"error":str(e)}, status =400)
        
        
