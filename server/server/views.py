from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import User, Dado, Sinal
from .serializer import UserSerializer, DadoSerializer, SinalSerializer
from django.http import HttpResponse

def index(request):
    users = User.objects.all()
    dados = Dado.objects.all()
    sinais = Sinal.objects.all()
    return render(request, 'index.html', context={'users': users, 'dados': dados, 'sinais':sinais})

class UserViewSet(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class DadoViewSet(viewsets.ModelViewSet):
    queryset = Dado.objects.all()
    serializer_class = DadoSerializer

class SinalViewSet(viewsets.ModelViewSet):
    queryset = Sinal.objects.all()
    serializer_class = SinalSerializer