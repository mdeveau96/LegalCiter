
from rest_framework import generics, permissions
from backend.models import Case, Cite, CustomUser
from backend.serializers import CaseSerializer, CiteSerializer, UserSerializer


class CaseList(generics.ListCreateAPIView):
    """
    List all cases
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class CiteList(generics.ListCreateAPIView):
    
    queryset = Cite.objects.all()
    serializer_class = CiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class CiteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a cite
    """
    queryset = Cite.objects.all()
    serializer_class = CiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
