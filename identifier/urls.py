from django.urls import path
from identifier import views

urlpatterns = [
	path('', views.ReportedMessageView.as_view(), name='reports'),
	path('<int:pk>/', views.ReviewMessageView.as_view(), name='review'),
]