import csv
import datetime
from io import TextIOWrapper
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView, status

from .models import Visit
from Patient.models import Patient
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


class UploadCSVView(generics.GenericAPIView):
    parser_classes = [MultiPartParser]
    def post(self, request, *args, **kwargs):
        try:
            file = request.FILES.get('file')
            if not file: 
                raise ValueError('No file found.')
            csv_file = TextIOWrapper(file, encoding='utf-8')
            reader = csv.DictReader(csv_file)
        except Exception as exception:
            return Response(
                {"error": f"{str(exception)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for row in reader:
            try:
                patient, created = Patient.objects.get_or_create(
                    mr_number=row['mr_number'],
                    defaults={
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'date_of_birth': row['dob'] or None,
                    }
                )
                Visit.objects.create(
                    patient=patient,
                    date=datetime.datetime.strptime(row['date'], "%Y-%m-%d %H:%M:%S"),
                    reason=row['reason'],
                )

            except IntegrityError:
                return Response(
                    {"error": f"Duplicate visit found for MR {row['mr_number']} on {row['date']}."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Exception as e:
                return Response(
                    {"error": f"Error processing row: {row}. Error: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response({"message": "File(s) uploaded successfully."}, status=status.HTTP_200_OK)