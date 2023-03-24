"""
Database models for courses_catalog.
"""

from django.db import models


class XCourses(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
