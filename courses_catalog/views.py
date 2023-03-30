from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses_catalog.models import XCourses
from rest_framework.generics import ListAPIView
from courses_catalog.serializers import XCoursesSerializer
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from lms.djangoapps.course_api.serializers import CourseSerializer

@api_view(['GET'])
def get_courses(request):

    courses = XCourses.objects.all()
    serializer = XCoursesSerializer(courses, many=True)
    return Response({'courses': serializer.data})


class CourseListAPIView(ListAPIView):

    queryset = CourseOverview.get_all_courses().prefetch_related(
        'modes',
    ).select_related(
        'image_set'
    )
    serializer_class = CourseSerializer

