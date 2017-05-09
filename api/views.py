# coding:utf-8
from __future__ import print_function
from django.shortcuts import render
from rest_framework import generics
from api.serializers import StudentSerializer
from .models import Student, StudentSorce
from rest_framework.response import Response
from rest_framework import status
from api.serializers import StudentSorceSerializer


# 学生列表
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # 创建一个student
    def create(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    def list(self, request, *args, **kwargs):
        print('list')
        return Response(StudentSerializer(Student.objects.filter(student_id__gt=102), many=True).data)
        '''


# 单个学生
class StudentDetail(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'name'

    # 得到一个数据集
    def get_queryset(self):
        return Student.objects.filter(name=self.kwargs['name'])

    # get方法返回一个student
    def get(self, request, *args, **kwargs):
        # 获取url中的参数
        # http://127.0.0.1:8000/api/students/aaa/?test=123
        # 取test的值
        print(self.request.GET.get('test', None))

        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            #'sorce': StudentSorceSerializer(StudentSorce.objects.all(), many=True).data
        })

    # 更新某一个学生的信息
    def update(self, request, *args, **kwargs):
        pass
