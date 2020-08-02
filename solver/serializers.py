from rest_framework import serializers
from .models import Solver

class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver
        fields = ('letters', 'size')