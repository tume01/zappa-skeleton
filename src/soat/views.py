from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LicensePlateSerializer
from rest_framework import status
from .models import LicensePlate


class ListLicensePlates(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request, format=None):
        """
        Return a list of all license plates.
        """
        if not LicensePlate.exists():
            LicensePlate.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        data = [element for element in LicensePlate.scan()]
        serializer = LicensePlateSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        plate = request.data.get('license_plate')
        license = LicensePlate(plate)
        license.save()
        serializer = LicensePlateSerializer(license)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
