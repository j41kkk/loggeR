import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):

    logger.error("Test YEP!!!")

    return HttpResponse("Hello it's my L0ggER!")