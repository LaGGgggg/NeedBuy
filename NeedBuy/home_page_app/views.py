from django.shortcuts import render

# Create your views here.


def view_index(request):

    match request.method:

        case 'GET':

            return render(request, 'home_page_app/index.html')
