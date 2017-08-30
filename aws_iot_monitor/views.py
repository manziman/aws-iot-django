# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Imports
from django.shortcuts import render
from django.http import JsonResponse
import boto3, json

# Views

def home(request):
	""" Home page """
	return render(request, 'aws_iot_monitor/home.html', {'nbar': 'home'})

def monitor(request):
    """ Monitor form """
    if request.method == "POST":
    	device_id = request.POST.get("id", "")
    	if len(device_id) > 255:
    		return render(request, 'aws_iot_monitor/monitor.html', {'search': False, 'nbar': 'monitor', 'err': 'invalid_id'})
    	client = boto3.client('iot')
    	try:
    		response = client.describe_thing(thingName=device_id)
    	except:
    		return render(request, 'aws_iot_monitor/monitor.html', {'search': False, 'nbar': 'monitor', 'err': 'not_found'})
    	return render(request, 'aws_iot_monitor/monitor.html', {'search': True, 'nbar': 'monitor', 'err': None, 'id': device_id})
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
	return render(request, 'aws_iot_monitor/about.html', {'nbar': 'about'})