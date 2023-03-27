from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses_catalog.models import XCourses
from courses_catalog.serializers import XCoursesSerializer


@api_view(['GET'])
def get_courses(request):

    courses = XCourses.objects.all()
    serializer = XCoursesSerializer(courses, many=True)
    return Response({'courses': serializer.data})
