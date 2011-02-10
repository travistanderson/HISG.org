# apps/training/__init__.py
from django.contrib.auth.models import User
from django.db.models import Q
from rpc4django import rpcmethod
from training.models import Event

@rpcmethod(name='login.add',)
def add(a,b):
	return a+b