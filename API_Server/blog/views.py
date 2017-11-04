from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from requests import Response


@csrf_exempt
def inputData(request):
    print(request)
    if request.method == 'GET':
        # request_data = ((request.body).decode('utf-8'))
        # request_data = json.loads(request_data)
        # content = request['content']
        print('18')
        print(request)
    # print('sdasds')
    a = "a"
    # return Response(a)
    return render(request, 'default_page.html')