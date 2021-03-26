from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from website import utils
from website.models import User
from website.serializers import SignupSerializer, LogoutSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()
    #
    # def perform_create(self, serializer):
    #     serializer.save()
    #     user_data = serializer.data

    def perform_create(self, serializer,request):
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email =user_data['email'] )
        token = RefreshToken.for_user(user)
        current_site = get_current_site(request)
        data = {'domain':current_site.domain}
        utils.send_email(data)



class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)




