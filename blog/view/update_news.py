from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import New
from blog.serializer.NewsSerializer import NewsAddSerializer


class NewsUpdateView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request,pk, format=None):
        try:
            news_object = New.objects.select_related("author").get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound("News not found")
        serializer = NewsAddSerializer(news_object,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({
            "message":"News updated"
        })
