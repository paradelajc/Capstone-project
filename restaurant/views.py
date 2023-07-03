from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from .models import MenuItem, Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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

def index(requests):
  return render(requests, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
  return Response({'message': 'This view is protected'})
