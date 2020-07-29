from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import Country
from django.http import Http404
# Create your views here.
# This is for Country Entity
class CountryList(APIView):
    # used for read data in the country entity
 def get(self,request):
    country=Country.objects.all()
    serializer=CountrySerializer(country,many=True)
    return Response(serializer.data)

 # used for create data in the country entity
 def post(self,request):
    serializer=CountrySerializer(data=request.data)
    if serializer.is_valid():
        if not Country.objects.filter(id=request.data.get('id')):
          serializer.save()
          return Response(serializer.data)
    return Response(status=status.HTTP_409_CONFLICT)

class CountryDetail(APIView):
#used for update data in the country entity
  def put(self,request,pk):
    country=Country.objects.get(id=pk)
    serializer=CountrySerializer(instance=country,data=request.data)
    if serializer.is_valid():
     #if  country.id == request.data.get('id',"key not found") and country.Name==request.data.get('Name',"key not found") :
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #used to delete data in the country entity
  def delete(self,request,pk):
    try:
       country = Country.objects.get(id=pk)
       country.delete()
       return ("Item deleted successfully")
    except:
       return Response(status=status.HTTP_204_NO_CONTENT)