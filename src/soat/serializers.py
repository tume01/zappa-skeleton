from rest_framework import serializers


class LicensePlateSerializer(serializers.Serializer):

    license_plate = serializers.CharField()