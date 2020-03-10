from rest_framework.decorators import api_view
from rest_framework.response import Response

from train.models import Train
from train.serializers import TrainSerializer


@api_view(['GET'])
def train_list(request):
    if request.method == 'GET':
        trains = Train.objects.all()

        serializer = TrainSerializer(trains, context={'request': request}, many=True)

        return Response({
            'data': serializer.data,
        })
