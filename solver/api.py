from solver.models import Solver
from rest_framework import viewsets, permissions
from .serializers import SolverSerializer

# Lead Viewset
class SolverViewSet(viewsets.ModelViewSet):
    queryset = Solver.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SolverSerializer
