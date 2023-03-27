"""
courses_catalog Django application initialization.
"""

from django.apps import AppConfig


class CoursesCatalogConfig(AppConfig):
    """
    Configuration for the courses_catalog Django application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses_catalog'
