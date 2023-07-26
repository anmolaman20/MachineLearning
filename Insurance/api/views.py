from django.shortcuts import render,HttpResponse

from rest_framework.decorators import api_view

from rest_framework.response import Response
import numpy as np
import joblib
import os

from .serializers import InsuranceSerializers




model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','Model','InsuranceCostPredictor.pkl')

model = joblib.load(model_path)

@api_view(['POST'])

def predict(request):
    if request.method == 'POST':
        #deserialre
        serializer = InsuranceSerializers(data= request.data)
        if serializer.is_valid():
            #convert the i/p data to i/p format for model
            input_data = tuple(serializer.validated_data.values())
            input_data_as_numpy_arrays = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_arrays.reshape(1,-1)
            print(input_data_reshaped)
        #make a prediction

        prediction = model.predict(input_data_reshaped)

        #return the prediction as JSOn response

        return Response(prediction)

def index(request):
    return HttpResponse("Hello")
    
    