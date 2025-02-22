from django.urls import path
from .views import VisitView


class AppointmentUrls:
    @staticmethod
    def get_urls():
        urls = [
            path('visit/', VisitView.as_view()),
        ]
        return urls
 