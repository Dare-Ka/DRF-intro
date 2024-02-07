# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializer


class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# class ShortSensorsInfoView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#
# class FullSensorsInfoListView(RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorsSerializer
#
#
# class MeasurementCreateView(RetrieveUpdateDestroyAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer
#
#
# class MeasurementsCreateView(ListCreateAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementsSerializer
#
