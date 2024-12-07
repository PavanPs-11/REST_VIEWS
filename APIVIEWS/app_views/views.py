from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from app_views.models import Student
from app_views.serializers import Student_Serializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView


# Create your views here.
@api_view()
def home(request):
    return Response("<h1> REST API VIEW <h1>")


@api_view()
def home2(request):
    data1 = Student.objects.all()
    serializer = Student_Serializer(data1, many=True)
    return Response({"pay": serializer.data})


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer


class StudentRet(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer


class StudentUp(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer


class Studentlc(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer
