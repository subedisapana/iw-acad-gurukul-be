from django.shortcuts import render

# Create your views here.
class AssignmentView(APIView):
    def post(self, request):
        serializer = AssignmentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)