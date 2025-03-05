
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static

from ebooking import views as v1
urlpatterns = [
    path('', v1.index, name='home'),
    path('view/',v1.views_booking, name='view'),
    path('update/<int:booking_id>/', v1.update_booking, name='update_booking'), 
    path('delete/<int:booking_id>/',v1.delete_booking, name='delete_booking'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)