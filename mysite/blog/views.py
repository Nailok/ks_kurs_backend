from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django_filters import Filter
from django_filters.fields import Lookup
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status
from .models import Client, DataTable, StudyDirection

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'updated', )


class DataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTable
        fields = ('id', 'firstname', 'lastname', 'address', 'phone', 'birthday', 'gender', 'updated', )

class StudyDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDirection
        fields = ('name',)

class DataTableFilter(filters.FilterSet):
    firstname = filters.CharFilter(field_name='firstname', lookup_expr='icontains')
    lastname = filters.CharFilter(field_name='lastname', lookup_expr='icontains')
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')
    phone = filters.CharFilter(field_name='phone', lookup_expr='icontains')
    birthday = filters.CharFilter(field_name='birthday', lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender', lookup_expr='icontains')


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.filter()
        return queryset



class StudyDirectionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StudyDirectionSerializer

    def get_queryset(self):
        queryset = StudyDirection.objects.filter()
        return queryset



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Client.objects.filter()
        return queryset

    @action(methods=['post'], detail=False)
    def reguser(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            return Response({"response": "User already exists"}, status=status.HTTP_304_NOT_MODIFIED)
        except User.DoesNotExist:
            try:
                User.objects.create_user(username=request.data['username'],
                                         email=request.data['email'],
                                         password=request.data['password'])
            except:
                return Response({"response": "Error"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"response": "okay"}, status=status.HTTP_200_OK)

class DataTableViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DataTableSerializer
    filter_class = DataTableFilter
    filter_backends = (DjangoFilterBackend, )


    def get_queryset(self):
        queryset = DataTable.objects.filter()
        return queryset

    # @action(methods=['post'], detail=False)
    # def reguser(self, request):
    #     try:
    #         user = User.objects.create_user(username=request.data['username'],
    #                                         email=request.data['email'],
    #                                         password=request.data['password'])
    #     except:
    #         return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({"response": "okay"}, status=status.HTTP_200_OK)

