from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import Case, Cite
from backend.serializers import CaseSerializer, CiteSerializer


@csrf_exempt
def case_list(request):
    """
    List all cases
    """
    if request.method == 'GET':
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return JsonResponse(serializer.data, safe=False)
    

def cite_list(request):
    if request.method == 'GET':
        cites = Case.objects.all()
        serializer = CiteSerializer(cites, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
