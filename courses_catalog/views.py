from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_courses(request):
    return Response({'message' : 'Returns a list of courses...'})
