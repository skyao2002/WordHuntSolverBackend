from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from solver.models import Solver
from solver.serializers import SolverSerializer
from solver.apps import SolverConfig
from solver.solver import solveWordHunt

@api_view(['POST'])
def solve_this(request):
    if SolverConfig.dictionaryLoaded: 
        serializer = SolverSerializer(data=request.data)
        if serializer.is_valid():
            letters = serializer.validated_data.get("letters").upper()
            solution = solveWordHunt(letters, serializer.validated_data.get("size"))
            return Response({"answer": solution.ansNoDuplicates}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Dictionary has not loaded yet. The server may be down. Wait a couple seconds and try again."}, status=status.HTTP_400_BAD_REQUEST)