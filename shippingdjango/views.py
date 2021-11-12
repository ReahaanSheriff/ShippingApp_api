from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from .serializers import *
from .models import *

# Create your views here.


@api_view(['GET','POST'])
def register(request):
    if request.method == 'GET':
        shipments = User.objects.all()
        serializer = RegisterSerializer(shipments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered"
            data['email'] = user.email
            data['username'] = user.username
            token = AuthToken.objects.create(user)[1]
            data['token'] = token
            data['password'] = user.password
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data
            data['username'] = user.username
            data['password'] = user.password
            token = AuthToken.objects.create(user)[1]
            data['token'] = token
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def createShipment(request):
    if request.method == 'GET':
        shipments = CreateShipment.objects.all()
        serializer = CreateShipmentSerializer(shipments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CreateShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userShipment(request):
    try:
        shipment = CreateShipment.objects.filter(user_id_id=request.user.id)
        serializer = CreateShipmentSerializer(shipment, many=True)
        return Response(serializer.data)
    except:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getShipment(request,pk):
    try:
        shipment = CreateShipment.objects.get(pk=pk)
    except CreateShipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreateShipmentSerializer(shipment)
        return Response(serializer.data)

@api_view(['POST'])   
def deletetokens(request):
    try:
        AuthToken.objects.all().delete()
        return Response(status=status.HTTP_201_CREATED)
    except AuthToken.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def trackAllShipment(request):
    if request.method == 'GET':
        shipments = Tracking.objects.all()
        serializer = TrackingSerializer(shipments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def trackOneShipment(request,fk):
    try:
        ship = Tracking.objects.get(shipment=fk)
    except Tracking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrackingSerializer(ship)
        return Response(serializer.data)