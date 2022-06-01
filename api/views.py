from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Items, Poll, Choice, Vote
from .serializers import ItemSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from .serializers import UserSerializer, PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth import authenticate

# Create your views here.


# class UserCreate(generics.CreateAPIView):
#     serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer


@api_view(['GET'])
def getData(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items, many=True)
    # person = {'chizzy': 'python', 'aluta': 'python', 'femi': 'python'}
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def itemDetails(request, pk):
    # item = Items.objects.get(id=pk)
    # serializer = ItemSerializer(item, many=False)
    # return Response(serializer.data)
    try:
        item = Items.objects.get(id=pk)
    except Items.DoesNotExist:
        return Response('Item not found in database...')
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def update_item(request, pk):
    try:
        item = Items.objects.get(id=pk)
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except Items.DoesNotExist:
        return Response('Item not found in database...')

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_item(request, pk):
    try:
        item = Items.objects.get(id=pk).delete()
    except Items.DoesNotExist:
        return Response('Item not found in database...')

    return Response("Successfully deleted")


# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)

# class PollList(generics.ListCreateAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer


# class PollDetail(generics.RetrieveDestroyAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
