from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets

from accounts.models import Student, Teacher
from accounts.serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, StudentSerializers, \
    TeacherSerializers
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()




# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all().order_by('-date_created')
    serializer_class = StudentSerializers

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Teacher.objects.all().order_by('-date_created')
    serializer_class = TeacherSerializers
