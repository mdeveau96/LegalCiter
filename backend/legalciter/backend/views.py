from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, viewsets, renderers
from backend.models import Case, Cite, CustomUser
from backend.serializers import CaseSerializer, CiteSerializer, UserSerializer


@api_view(['GET'])
def api_root(request, format=None) -> Response:
    return Response({
        'users': reverse('customuser-list', request=request, format=format),
        'cases': reverse('case-list', request=request, format=format),
        'cites': reverse('cite-list', request=request, format=format)
    })


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CiteViewSet(viewsets.ModelViewSet):
    queryset = Cite.objects.all()
    serializer_class = CiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
