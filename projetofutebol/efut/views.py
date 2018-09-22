from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, UsuariosSerializer, TimesSerializer, LancesSerializer, LocaisSerializer, \
    PartidasSerializer
from .models import Usuarios, Partidas, Lances, Locais, Times


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class TimesViewSet(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimesSerializer


class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partidas.objects.all()
    serializer_class = PartidasSerializer


class LancesViewSet(viewsets.ModelViewSet):
    queryset = Lances.objects.all()
    serializer_class = LancesSerializer


class LocaisViewSet(viewsets.ModelViewSet):
    queryset = Locais.objects.all()
    serializer_class = LocaisSerializer

