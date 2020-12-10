from django.urls import path

from blog.view.add_news import NewsAddView
from blog.view.delete_news import DeleteView
from blog.view.get_list_news import FilteredNews
from blog.view.get_news import NewsDetail
from blog.view.update_news import NewsUpdateView

urlpatterns = [
    path('add/news/', NewsAddView.as_view(), name='add_news'),
    path('get/news/<int:pk>/', NewsDetail.as_view(), name='detail'),
    path('delete/news/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('update/news/<int:pk>/', NewsUpdateView.as_view(), name='update'),
    path('list/news/', FilteredNews.as_view(), name='list_news'),


]