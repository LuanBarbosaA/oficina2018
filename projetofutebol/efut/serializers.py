from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuarios, Lances, Locais, Partidas, Times


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class TimesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Times
        fields = '__all__'


class LocaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locais
        fields = '__all__'


class PartidasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partidas
        fields = '__all__'


class LancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lances
        fields = '__all__'