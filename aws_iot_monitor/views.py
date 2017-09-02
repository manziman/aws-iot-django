# -*- coding: utf-8 -*-
from __future__ 		import unicode_literals

# Imports
import boto3, json
from django.shortcuts 	import render
from django.http 		import JsonResponse
from .forms 			import DeviceSearch

# Views

def home(request):
	""" Home page """
	return render(request, 'aws_iot_monitor/home.html', {'nbar': 'home'})

def monitor(request):
    """ Device search form """
    if request.method == "POST":
    	form = DeviceSearch(request.POST)
    	if not form.is_valid():
    		return render(request, 'aws_iot_monitor/monitor.html', {'search': False, 'nbar': 'monitor', 'err': 'invalid_id'})
    	# Open boto3 client connection to AWS IoT
    	client = boto3.client('iot')
    	# Try to pull the information on the thing from IoT, if not then return error
    	try:
    		response = client.describe_thing(thingName=form.cleaned_data['devid'])
    	except:
    		return render(request, 'aws_iot_monitor/monitor.html', {'search': False, 'nbar': 'monitor', 'err': 'not_found', 'id': form.cleaned_data['devid']})
    	return render(request, 'aws_iot_monitor/monitor.html', {'search': True, 'nbar': 'monitor', 'err': None, 'id': form.cleaned_data['devid']})
    else:
    	return render(request, 'aws_iot_monitor/monitor.html', {'search': False, 'nbar': 'monitor', 'err': None})

def monitor_update(request):
	""" Response to AJAX request for update on device status """
	device_id = request.POST.get("id", "")
	client = boto3.client('iot-data')
	response = client.get_thing_shadow(thingName=device_id)
	d = response[u'payload'].read()
	d = json.loads(d)
	d = d[u'state']
	return JsonResponse(d)

def about(request):
	""" Placeholder about page """
	return render(request, 'aws_iot_monitor/about.html', {'nbar': 'about'})