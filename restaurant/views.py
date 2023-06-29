from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.

# class MenuView(APIView):
#   def get(self, request):
#     items = Menu.objects.all()
#     serializer = MenuSerializer(items, many=True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer = MenuSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response({'status': 'success', 'data':serializer.data})

# class BookingView(APIView):
#   pass

class MenuItemsView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer