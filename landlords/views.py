from django.shortcuts import render_to_response
from landlords.models import Landlord, Room, Message
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext
from landlords.forms import MessageForm

# def room(request):
# 	path = request.path
# 	landlord = Landlord.objects.get(id=1)
# 	return render_to_response('room.html', locals())

def room(request):
	if 'id' in request.GET and request.GET['id'] != '':
		landlord = Landlord.objects.get(id=request.GET['id'])
		return render_to_response('room.html', locals())
	else:
		return HttpResponseRedirect("/landlords_list/")

# def room(request, id):
# 	if id:
# 		landlord = Landlord.objects.get(id=id)
# 		return render_to_response('room.html', locals())
# 	else:
# 		return HttpResponseRedirect("/landlords_list/")

def list_landlords(request):
	landlords = Landlord.objects.all()
	return render_to_response('landlord_list.html', locals())

def message(request, id):
	if id:
		l = Landlord.objects.get(id=id)
	else:
		return HttpResponseRedirect("/landlords_list/")
	if request.POST:
		f = MessageForm(request.POST)
		if f.is_valid():
			potential_tenant = request.POST['potential_tenant']
			content = request.POST['content']
			email = request.POST['email']
			date_time = timezone.localtime(timezone.now()) # get the current timezone
			c = Message.objects.create(
				potential_tenant = potential_tenant,
				email = email,
				content = content,
				date_time = date_time,
				landlord = l
				)
			f = MessageForm(initial={'content':'Please enter why you need the room and how this room suite your need.'})
	else:
		f = MessageForm(initial={'content':'Please enter why you need the room and how this room suite your need.'})
	return render_to_response('message.html', RequestContext(request, locals()))