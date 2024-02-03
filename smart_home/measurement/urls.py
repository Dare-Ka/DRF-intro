from django.urls import path
from measurement.views import ShortSensorsInfoView, FullSensorsInfoListView, MeasurementCreateView, MeasurementsCreateView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ShortSensorsInfoView.as_view()),
    path('sensors/<pk>/', FullSensorsInfoListView.as_view()),
    path('measurements/<pk>', MeasurementCreateView.as_view()),
    path('measurements/', MeasurementsCreateView.as_view()),
]
