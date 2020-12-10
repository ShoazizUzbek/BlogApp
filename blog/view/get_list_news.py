from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import New
from blog.serializer.FIlterSerializer import FilterSerializer


class FilteredNews(APIView):

    permission_classes = (AllowAny,)

    def post(self,request):
        serializer = FilterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        tags = validated_data.get("tags")
        added_at = validated_data.get("added_at")
        filter_set = {}
        if tags:
            filter_set = {
                "tags__in":tags
            }
        if added_at:
            filter_set.update({
                "added_at":added_at
            })
        news = New.objects.prefetch_related("news_name").\
            filter(**filter_set)
        data = []
        for new in news:
            data.append({"pk":new.pk})
        return Response(data)
