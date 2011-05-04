# apps/training/__init__.py
from django.contrib.auth.models import User
from django.db.models import Q
from rpc4django import rpcmethod
from training.models import Event
from datetime import datetime

@rpcmethod(name='training.add',)
def add(a,b):
	return a+b
	
	
@rpcmethod(name='training.events',)
def events():
	ue = Event.objects.filter(start_date__gte = datetime.now())
	pe = Event.objects.filter(start_date__lt = datetime.now())
	events = []
	uevents = []
	pevents = []
	for event in ue:
		theevent = {}
		# theevent['name'] = event.name
		theevent['contact'] = event.contact.email
		theevent['subject'] = event.subject
		theevent['start_date'] = event.start_date.strftime('%b. %d, %Y')
		theevent['end_date'] = event.end_date.strftime('%b. %d, %Y')
		theevent['location'] = event.location
		theevent['latitude'] = event.latitude
		theevent['longitude'] = event.longitude
		# theevent['description'] = event.description
		theevent['active'] = event.active
		uevents.append(theevent)
	for event in pe:
		theevent = {}
		# theevent['name'] = event.name
		theevent['contact'] = event.contact.email
		theevent['subject'] = event.subject
		theevent['start_date'] = event.start_date.strftime('%b. %d, %Y')
		theevent['end_date'] = event.end_date.strftime('%b. %d, %Y')
		theevent['location'] = event.location
		theevent['latitude'] = event.latitude
		theevent['longitude'] = event.longitude
		# theevent['description'] = event.description
		theevent['active'] = event.active
		pevents.append(theevent)
	events.append(uevents)
	events.append(pevents)
	
	return events
	
	
	
