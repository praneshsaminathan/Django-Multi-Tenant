from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyUser
# Create your views here.
from .serializer import MyUserSerializer
from .tasks import async_temp


class MyUserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = (AllowAny,)


class TempAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        # import pdb; pdb.set_trace()
        async_temp.delay("delayy")

        return Response(data={"message": "Completed"}, status=status.HTTP_200_OK)