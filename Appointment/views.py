from rest_framework.views import APIView, status
from django.http import JsonResponse
from .models import Visit
from .serializers import VisitSerializer

class VisitView(APIView):
    def get(self, request):
        success, data, msg = False, None, "Something went wrong! Please try again later." 
        try:
            query_visit = Visit.objects.all().order_by('date')
            data = VisitSerializer(query_visit, many=True).data
            msg = "ok"
            success = True
        except Exception as exception:
            success = False
            data = None
            msg = str(exception)
        return JsonResponse({"issuccess": success, "msg": msg, "data": data}, safe=False)
