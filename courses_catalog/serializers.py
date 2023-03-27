from rest_framework import serializers
from courses_catalog.models import XCourses


class XCoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = XCourses
        fields = ('id', 'title', 'course_code', 'description',)
