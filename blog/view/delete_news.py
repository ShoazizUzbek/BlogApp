from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import New


class DeleteView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, pk):
        try:
            news_object = New.objects.select_related("author").get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound("News not found")
        news_object.delete()
        return Response(
            {"message":"news successfully deleted"}
        )
