from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer
from .models import User
from .permissions import ReadOnly
from .generics import BasicListCreateAPIView, BasicRetrieveUpdateDestroyAPIView
import logging
import shortuuid
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
logger = logging.getLogger(__name__)


class UserListCreateView(BasicListCreateAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        data['id'] = shortuuid.uuid()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'data': serializer.data,
                'code': 0,
            },
            status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserDetailView(BasicRetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
