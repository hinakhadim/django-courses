"""
courses_catalog Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import (
    PluginURLs
)

from openedx.core.djangoapps.plugins.constants import ProjectType


class CoursesCatalogConfig(AppConfig):
    """
    Configuration for the courses_catalog Django application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses_catalog'

    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'courses_catalog',
                PluginURLs.REGEX: r'^api/courses_catalog/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }

    # plugin_app = {
    #     'url_config': {
    #         'lms.djangoapp': {
    #             'namespace': 'courses_catalog',
    #             'regex': 'api/courses_catalog/',
    #             'relative_path': 'urls',
    #         }
    #     },
    # }
