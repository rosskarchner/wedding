from django.shortcuts import render_to_response, redirect
from  django.template import RequestContext, TemplateDoesNotExist
from django.http import Http404

from models import Song

from forms import LoginForm, SongForm



def login(request):
	
	if request.method == 'POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			request.session['logged_in']='yes'
			return redirect('front')
			
		
	else:
		if request.session.get('logged_in', False):
			return redirect('front')
		form=LoginForm()

	return render_to_response('login.html', locals(), context_instance=RequestContext(request))
	
def logout(request):
	try: 
		del request.session['logged_in']
	except KeyError:
		pass
	return redirect('login')
	
	
	
def songs(request):
	if request.method== 'POST':
		form=SongForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('songs')
	else:
		form=SongForm()
	
	songs=Song.objects.all().order_by('-added_on')
	return render_to_response('songs.html' , locals(), context_instance=RequestContext(request))
	
def getpage(request, name="index"):
	if not request.session.get('logged_in'): return redirect('login')
	try:
		return render_to_response('%s.html' % name, locals(), context_instance=RequestContext(request))
	except TemplateDoesNotExist:
		raise Http404 