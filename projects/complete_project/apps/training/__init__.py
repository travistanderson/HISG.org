# apps/training/__init__.py
from django.contrib.auth.models import User
from django.db.models import Q
from rpc4django import rpcmethod
from training.models import Event

@rpcmethod(name='training.add',)
def add(a,b):
	return a+b
	
	
@rpcmethod(name='training.events',)
def events():
	e = Event.objects.all()
	events = []
	for event in e:
		theevent = {}
		theevent['name'] = event.name
		theevent['contact'] = event.contact
		theevent['subject'] = event.subject
		theevent['start_date'] = event.start_date
		theevent['end_date'] = event.end_date
		theevent['location'] = event.location
		theevent['latitude'] = event.latitude
		theevent['longitude'] = event.longitude
		theevent['description'] = event.description
		theevent['active'] = event.active
		events.append(theevent)
	
	return events
	
	
	
