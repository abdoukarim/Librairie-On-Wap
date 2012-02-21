# Create your views here.
from librairie.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.safestring import SafeUnicode

 
def toggle_monthTheme(request, id):
  theme = Theme.objects.get(pk=id)
  theme.monthTheme = not theme.monthTheme
  theme.save()
  return HttpResponseRedirect(reverse("admin:librairie_theme_changelist"))

def sujet(request):
	theme_mois = Theme.objects.get(monthTheme=True) #on choisit le sujet du mois!	
	authorz = Author.objects.get(status=True)
	title = Livre.objects.get(authors=authorz)
	resume = SafeUnicode(title.resume[0:1000]) #on recupere les 1000 premiers caracteres
	resume2 = SafeUnicode(title.resume[1000:2000])
	liste_ouvragres = Livre.objects.filter(theme=theme_mois)[:4]
	
	#theme = Theme.objects.all()
	return render_to_response(
         'mobile/sujet.html',{'theme_mois' : theme_mois, 'authorz': authorz, 'title': title, 'liste_ouvragres' : liste_ouvragres,
											'resume' : resume, 'resume2' : resume2} )
	
def new(request):
	last = Livre.objects.order_by('id').reverse()[:5] #on recupere les 5 derniers livres
	lasts = last
	return render_to_response(
         'mobile/new.html', {'lasts' : lasts})
     
def detail(request, id):
	livre = Livre.objects.get(id=id)
	auteurs = livre.authors.all()
	#authorz = Author.objects.get(id=livre)
	#title = Livre.objects.get(id=id)
	
	return render_to_response('mobile/detail.html', {'livre' : livre, 'auteurs' : auteurs })

def resume(request, id):
	livre = Livre.objects.get(id=id)
	resume = SafeUnicode(livre.resume[0:1000]) #on recupere les 1000 premiers caracteres
	#resume2 = SafeUnicode(livre.resume[500:700])
	return render_to_response('mobile/resume.html', {'livre' : livre, 'resume' : resume}) 
	
def resume2(request, id):
	livre = Livre.objects.get(id=id)
	#resume = SafeUnicode(livre.resume[0:1000]) #on recupere les 1000 premiers caracteres
	resume2 = SafeUnicode(livre.resume[1000:5000])
	return render_to_response('mobile/resume2.html', {'livre' : livre, 'resume2' : resume2}) 
	
def search(request):
	themes = Theme.objects.all()
	return render_to_response(
         'mobile/search.html', {'themes' : themes }
     )
     
def contact(request):
	return render_to_response('mobile/contact.html')
