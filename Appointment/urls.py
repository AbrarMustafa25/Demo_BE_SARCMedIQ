from django.urls import path
from .views import VisitView, UploadCSVView


class AppointmentUrls:
    @staticmethod
    def get_urls():
        urls = [
            path('visit/', VisitView.as_view()),
            path('upload/', UploadCSVView.as_view()),
        ]
        return urls
 