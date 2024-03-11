from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import User,Store
from .serializers import UserSerializer, StoreSerializer
from rest_framework.permissions import AllowAny
from store_app.permissions import IsAdmin

class UserListView(ModelViewSet):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all()
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdmin]