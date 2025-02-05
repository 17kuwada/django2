from django.urls import path

# 同一フォルダ内のviews.pyを参照する
from . import views

app_name = 'diary'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('inquiry/',views.InquiryView.as_view(),name='inquiry'),
    path('diary_list/', views.DiaryListView.as_view(), name='diary_list'),
    
    path('diary_detail/<int:pk>', views.DiaryDetailView.as_view(), name='diary_detail'),
    # <int:pk>はモデル「Diary」クラスで用意されている 主キー値
    path('diary_create/',views.DiaryCreateView.as_view(),name='diary_create'),
    path('diary_update/<int:pk>/',views.DiaryUpdateView.as_view(),name='diary_update'),
    path('diary_delete/<int:pk>/',views.DiaryDeleteView.as_view(),name='diary_delete'),
]

