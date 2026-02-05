from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully"})


@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    try:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return Response({"message": "Wrong password"})
    except:
        return Response({"message": "User not found"})

    refresh = RefreshToken.for_user(user)

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    })



def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")
