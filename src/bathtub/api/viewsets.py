from rest_framework import viewsets, routers, response

from bathtub.common import models
from bathtub.api import serializers

router = routers.DefaultRouter()

class ShowViewSet(viewsets.ModelViewSet):
    model = models.Show
router.register(r'shows', ShowViewSet)

# class CharacterViewSet(viewsets.ModelViewSet):
#     model = models.Character
#
#     def list(self, request):
#         if('term' in request.GET):
#             queryset = models.Character.objects.filter(full_name__icontains=request.GET.get('term'))
#         else:
#             queryset = models.Character.objects.all()
#         serializer = serializers.CharacterSerializer(queryset, many=True)
#         return response.Response(serializer.data)
#
# router.register(r'characters', CharacterViewSet)
