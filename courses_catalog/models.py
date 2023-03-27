"""
Database models for courses_catalog.
"""

from django.db import models


class XCourses(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
