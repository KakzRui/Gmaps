from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
import json as simplejson
from localities.models import Locality
from django.template.loader import render_to_string
import logging
from django.views.decorators.csrf import csrf_protect

logger = logging.getLogger('Gmaps')

logger.info("Application Started")
@csrf_protect
def index(request):
	'Display map'
	localities = Locality.objects.order_by('name')
	return render_to_response('localities/index.html', {
		'localities': localities,
        'content': render_to_string('localities/localities.html', {'localities': localities}),
		})
@csrf_protect
def save(request):
	'Save localities'
	logger.info("Saving the address")
	for localityString in request.POST.get('localitiesPayload', '').splitlines():
		localityID, localityX, localityY = localityString.split()
		locality = Locality.objects.get(id = int(localityID))
		locality.geometry.set_x(float(localityX))
		locality.geometry.set_y(float(localityY))
		# logger.debug("Gemetry: %s" %(locality))
	return HttpResponse(simplejson.dumps(dict(isOk=1)))
