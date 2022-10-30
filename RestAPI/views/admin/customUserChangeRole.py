from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from RestAPI.serializers import UserSerializers
from RestAPI.services.main.admin.role_assignment import CustomUserChangeRoleServices


class CustomUserChangeRoleView(generics.ListAPIView):
    serializer_class = UserSerializers

    @permission_classes([IsAuthenticated])
    def post(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            outcome = CustomUserChangeRoleServices.execute(request.POST)
            if type(outcome) == str:
                return Response({"user": outcome}, status=status.HTTP_200_OK)
            else:
                return Response({"user": UserSerializers(outcome, many=False).data}, status=status.HTTP_200_OK)
        else:
            return Response({"user": "You don't have enough rights"}, status=status.HTTP_200_OK)