from pagos.models import Pagos, Services, PaymentUser, ExpiredPayments
from rest_framework import viewsets, status, filters
from .serializers import PagoSerializer, ServicesSerializer, PaymentUserSerializer, ExpiredPaymentsSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .pagination import StandardResultsSetPagination

class PagosViewSetCustom(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer(self):
        return PagoSerializer

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = PagoSerializer(data=request.data, many=True)
        else:
            serializer = PagoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pagos = get_object_or_404(self.queryset, pk=pk)
        serializer = PagoSerializer(pagos)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pagos = get_object_or_404(self.queryset, pk=pk)
        serializer = PagoSerializer(pagos, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pagos = get_object_or_404(self.queryset, pk=pk)
        serializer = get_object_or_404(pagos, self.queryset, pk=pk)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pagos = get_object_or_404(self.queryset, pk=pk)
        pagos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServicesViewSetCustom(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer(self):
        return ServicesSerializer

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = ServicesSerializer(data=request.data, many=True)
        else:
            serializer = ServicesSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        services = get_object_or_404(self.queryset, pk=pk)
        serializer = ServicesSerializer(services)
        return Response(serializer.data)

    def update(self, request, pk=None):
        services = get_object_or_404(self.queryset, pk=pk)
        serializer = ServicesSerializer(services, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        services = get_object_or_404(self.queryset, pk=pk)
        serializer = get_object_or_404(services, self.queryset, pk=pk)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        services = get_object_or_404(self.queryset, pk=pk)
        services.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentUserViewSetCustom(viewsets.ModelViewSet):
    queryset = PaymentUser.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer(self):
        return PaymentUserSerializer

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = PaymentUserSerializer(data=request.data, many=True)
        else:
            serializer = PaymentUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializer(payment_user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializer(payment_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        serializer = get_object_or_404(payment_user, self.queryset, pk=pk)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        payment_user = get_object_or_404(self.queryset, pk=pk)
        payment_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExpiredViewSetCustom(viewsets.ModelViewSet):
    queryset = ExpiredPayments.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_serializer(self):
        return ExpiredPayments

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if isinstance(request.data, list):
            serializer = PaymentUserSerializer(data=request.data, many=True)
        else:
            serializer = PaymentUserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        expired_payments = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializer(expired_payments)
        return Response(serializer.data)

    def update(self, request, pk=None):
        expired_payments = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializer(expired_payments, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        expired_payments = get_object_or_404(self.queryset, pk=pk)
        serializer = get_object_or_404(expired_payments, self.queryset, pk=pk)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        expired_payments = get_object_or_404(self.queryset, pk=pk)
        expired_payments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)