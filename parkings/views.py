from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .services import AssingParkingLotService

class UserParking(APIView):
    """
    View to list all users in the system.
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        try:
            service = AssingParkingLotService(request.data)
            return Response(service.get_week_schedule())
        except Exception as ex:
            return Response(str(ex))
