import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def view_index(request):

    match request.method:

        case 'GET':

            return render(request, 'home_page_app/index.html')

        case _:

            logger.error('Error request method.')

            return render(request, 'error.html')
