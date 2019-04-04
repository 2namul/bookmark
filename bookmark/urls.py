from django.urls import path
from .views import *
urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    #bookmark/이하 부분이 없을 떄, BookmarkListView를 호출
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),

]