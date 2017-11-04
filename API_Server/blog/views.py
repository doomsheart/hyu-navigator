from django.shortcuts import render
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def inputData(request):
    print(request)
    if request.method == 'POST':
        # request_data = ((request.body).decode('utf-8'))
        # request_data = json.loads(request_data)
        content = request.POST['content']
        print('18')
        print(content)
    print('sdasds')
    return render(request, 'default_page.html')