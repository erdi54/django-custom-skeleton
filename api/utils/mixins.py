from rest_framework import permissions, status, views, viewsets
from abc import ABCMeta, abstractstaticmethod
from api.utils.paginations import PaginationHandlerMixin
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CustomViewsetMixin(PaginationHandlerMixin):
    serializer_class = None
    serializer = None
    queryset = None
    pagination_class = None
    model_response = openapi.Response('response description', serializer)

    def list(self, request):
        pass

    @swagger_auto_schema(
        manual_parameters=[],
        query_serializer=serializer,
        responses={
            '200': model_response,
            '400': 'Bad Request'
        },
        security=[],
        operation_id='List API ',
        operation_description='List API',
    )
    def get(self, request, format=None):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(self.queryset.all(), many=True).data)
        else:
            serializer = self.serializer_class(self.queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=serializer,
        query_serializer=serializer,
        responses={
            '200': 'Ok Request',
            '400': "Bad Request"
        },
        security=[],
        operation_id='Create API ',
        operation_description='Create API',
    )
    def post(self, request, format=None):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
