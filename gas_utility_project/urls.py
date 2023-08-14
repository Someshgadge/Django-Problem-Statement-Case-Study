from django.urls import path
from customer_services import views  
from customer_services.views import submit_request, track_requests, update_request

app_name = 'customer_services'

urlpatterns = [
    path('submit-request/', views.submit_request, name='submit_request'),
    path('track-requests/', views.track_requests, name='track_requests'),
    path('update-request/<int:request_id>/', views.update_request, name='update_request'),  
]
