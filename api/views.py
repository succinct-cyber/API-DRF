from rest_framework.views import APIView
from cadence.models import Cadence
from employees.models import Employee
from .serializers import CadenceSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import mixins, generics


@api_view(['GET', 'POST'])
def CadenceView(request):
    if request.method == 'GET':
        # Get all the data from the Cadence Table
        cadence = Cadence.objects.all()
        serializer = CadenceSerializer (cadence, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CadenceSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400)

@api_view(['GET', 'PUT', 'DELETE'])   
def CadenceDetailView(request, pk):
    try:
        cadence = Cadence.objects.get(pk=pk)
    except Cadence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CadenceSerializer (cadence)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = CadenceSerializer (cadence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cadence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class EmployeeList(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:

#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             Employee.objects.get(pk=pk)
#         except:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

#     def delete(self, request, pk):
#         employee = self.get_object(pk=pk)
#         employee.delete()
#         return Response (status=status.HTTP_204_NO_CONTENT)


# class EmployeeList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get (self, request):
#         return self.list(request)

#     def post (self, request):
#         return self.create(request)

# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get (self, request, pk):
#         return self.retrieve(request, pk)

#     def put (self, request, pk):
#         return self.update(request, pk)
    
#     def delete (self, request, pk):
#         return self.destroy(request, pk)

# Generics
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Generics
class EmployeeDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer    



