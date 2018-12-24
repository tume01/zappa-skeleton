from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class LicensePlate(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = "licence_plate"
        host = 'http://dynamo:8000'

    license_plate = UnicodeAttribute(hash_key=True)