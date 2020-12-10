from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializer.NewsSerializer import NewsAddSerializer


class NewsAddView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = NewsAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
