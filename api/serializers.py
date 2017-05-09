# coding=utf-8
from rest_framework import serializers
from api.models import Student, StudentSorce


class StudentSorceSerializer(serializers.ModelSerializer):
    avg = serializers.SerializerMethodField('get_avg_sorce')

    class Meta:
        model = StudentSorce
        fields = ('math', 'english', 'chiness', 'avg')

    # 自定义方法构造的字段
    def get_avg_sorce(self, obj):
        return (obj.math + obj.english + obj.chiness) / 3.0


class StudentSerializer(serializers.ModelSerializer):
    sorce = serializers.SerializerMethodField('get_student_sorce')

    class Meta:
        model = Student
        fields = ('id', 'student_id', 'name', 'age', 'sorce')

    # 使用学号查出该学生的成绩
    def get_student_sorce(self, obj):
        print obj.student_id
        return StudentSorceSerializer(StudentSorce.objects.filter(student_id=obj.student_id), many=True).data
