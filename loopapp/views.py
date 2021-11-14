from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.



def index(request):
    return render(request, 'index.html')


@csrf_exempt
def loop_function_url(request):
    hidden_number = request.POST.get('hidden_number')
    print(hidden_number)
    print('hidden_number')
    return HttpResponse(True)


