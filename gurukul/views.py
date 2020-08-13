from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gurukul.serializers import UserSerializer

@api_view(['POST'])
def api_user_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            new_account = serializer.save()
            data['response'] = "user registered successfully"
            data['email'] = new_account.email
            data['first_name'] = new_account.first_name
            data['middle_name'] = new_account.middle_name
            data['last_name'] = new_account.last_name
        else:
            data = serializer.errors
        print(data,'*************')
        return Response(data)
 