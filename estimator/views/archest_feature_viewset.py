from rest_framework.decorators import action
from rest_framework.response import Response

from estimator.models import Feature
from estimator.serializers import FeatureSerializer
from estimator.services import feature
from estimator.views.archest_authenticated_model_viewset import ArchestAuthenticatedModelViewSet


class FeatureViewSet(ArchestAuthenticatedModelViewSet):
    """
    API endpoint that allows Features to be viewed or edited.
    """

    queryset = Feature.objects.none()

    def get_queryset(self):
        return feature.get_records(self.request)

    serializer_class = FeatureSerializer

    def create(self, request, *args, **kwargs):
        feature_object = Feature.objects.create(
            name=request.data['name'],
            phase_id=request.data['phase_id'],
        )  # type:Feature
        feature_serializer = self.get_serializer(feature_object, data=request.data, partial=True)
        feature_serializer.is_valid(raise_exception=True)
        feature_serializer.save()
        return Response(feature_serializer.data)

    def update(self, request, *args, **kwargs):
        """
        TODO: Refactor this function to handle validations properly. Also should be generic.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        partial = kwargs.pop('partial', False)

        feature_obj = self.get_object()  # type:Feature
        if 'name' in request.data:
            feature_obj.name = request.data['name']

        feature_serializer = self.get_serializer(feature_obj, data=request.data, partial=partial)
        feature_serializer.is_valid(raise_exception=True)
        feature_serializer.save()
        return Response(feature_serializer.data)

    @action(detail=False, methods=['patch'])
    def batch_delete_features(self, request):
        deleted_count = feature.delete_features(request.data['featureIds']);
        return Response({"results": deleted_count})
