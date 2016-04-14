from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext

def meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>{0}</td><td>{1}</td></tr>'.format(k ,v))
	return HttpResponse('<table>{0}</table>'.format('\n'.join(html)))

def welcome(request):
	if 'user_name' in request.GET and request.GET['user_name'] != '':
		return HttpResponse('Welcome!~' + request.GET['user_name'])
	else:
		return render_to_response('welcome.html', locals())

def set_c(request):
	response = HttpResponse('Set your lucky number as 8')
	response.set_cookie('lucky_number', 8)
	return response

def get_c(request):
	if 'lucky_number' in request.COOKIES:
		return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
	else:
		return HttpResponse('No cookies.')

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/index/')
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('login.html', RequestContext(request, locals()))

def index(request):
	return render_to_response('index.html', RequestContext(request, locals()))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/index/')