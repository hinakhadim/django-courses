"""
URLs for courses_catalog.
"""
from django.urls import re_path, path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from courses_catalog.views import get_courses

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="courses_catalog/base.html")),
    path(
        'list/', get_courses, name='get_courses_list'
    ),
]
