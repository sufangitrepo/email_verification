from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import MyUserRegisterSerializer, UserLoginSerializer

from .models import MyUser



class UserRegisterView(APIView):

    def post(self, request):
        
        register_serializer = MyUserRegisterSerializer(data=request.data)
        register_serializer.is_valid(raise_exception=True)
        user = register_serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token), 'id':user.id})




class VerifyEmailView(APIView):

    def get(self, request, uid):
        try:
            user:MyUser = MyUser.objects.get(email_verfication_token=uid)
            user.is_email_verified = True
            user.save()
            return Response({'message': 'verified'})
        except MyUser.DoesNotExist:
            return Response({'error': 'token is invalid'})    
        

class UserLoginView(APIView):


    def post(self, request):
       
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email and not password:
            return Response({'error':'email and password are required'})
        elif not email:
            return Response({'error':'email is required'})
        elif not password: 
            return Response({'error':'password is required'})
        
        try:
            user:MyUser = MyUser.objects.get(email=email)
            if not user.is_email_verified:
                return Response({'error': 
                                'email is not verified! check your email'})
            if user.check_password(raw_password=password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'message': 'logi successfully', 'token':str(token)})
            else:
                return Response({'error':'passwor is not correct'})
        except MyUser.DoesNotExist:
            return Response({'error': 'user with this email doesnot exist'})
            


    



