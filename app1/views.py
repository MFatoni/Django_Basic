from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from app1.models import Dreamreal
from django.core.mail import send_mail, send_mass_mail, mail_admins, mail_managers, EmailMessage
from django.views.generic import TemplateView
from app1.forms import LoginForm
from app1.forms import ProfileForm
from app1.models import Profile

def hello(request):
	today=datetime.now()
	daysOfWeek=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
	# return render(request, "hello.html",{"today":today, "days_of_week":daysOfWeek })
	return redirect('https://www.djangoproject.com')

def viewArticle(request, articleId):
	text= "<h1>Article Number : %s</h1>" % articleId
	# return HttpResponse(text)
	# return redirect(viewArticles, year = '2045', month = '02')
	return redirect('articles', year = '2045', month = '02')

def viewArticles(request, year, month):
	text= "<h1>Article Date : %s/%s</h1>" %(year,month)
	return HttpResponse(text)
# Create your views here.

def crudops(request):
	dreamreal=Dreamreal(
		website = "www.polo.com", mail = "sorex@polo.com", name = "sorex", phonenumber="08998566771"
	)
	dreamreal.save()

	objects= Dreamreal.objects.all()
	res = 'Printing all Dreamreal entries in the DB : <br>'

	for elt in objects:
		res += elt.name + "<br>"

	sorex = Dreamreal.objects.get(name = "sorex")
	res += 'Printing one entry'
	res += sorex.name

	res += '<br> Deleting an entry <br>'
	sorex.delete()

	dreamreal = Dreamreal( 
		website = "www.polo.com", mail = "sorex@polo.com", name = "sorex", phonenumber="08998566771"
	)

	dreamreal.save()
	res += 'Updating entry <br> '

	dreamreal = Dreamreal.objects.get(name = 'sorex')
	dreamreal.name = 'thierry'
	dreamreal.save()

	return HttpResponse(res)

def datamanipulation(request):
	res = ''

	qs = Dreamreal.objects.filter(name = "paul")
	res += "Found : %s results <br>" %len(qs)

	qs=Dreamreal.objects.order_by("name")
	for elt in qs:
		res += elt.name + '<br>'

	return HttpResponse(res)

def sendSimpleEmail(request, emailto):
	res = send_mail("Hello Paul","tes123","fatoni.testing@gmail.com",[emailto])
	return HttpResponse('%s'%res)

def sendMassEmail(request, emailto1,emailto2):
	msg1=('subject1' , 'message 1' , 'fatoni.testing@gmail.com', [emailto1])
	msg2=('subject2' , 'message 2' , 'fatoni.testing@gmail.com', [emailto2])
	res = send_mass_mail((msg1 , msg2), fail_silently = False)
	return HttpResponse('%s' %res)

def sendAdminsEmail(request):
	res = mail_admins('my subject', 'site is going down',)
	return HttpResponse('%s' %res)

def sendManagersEmail(request):
	res = mail_managers('my subject 2', 'Change date on the site.')
	return HttpResponse('%s' %res)

def sendHTMLEmail(request, emailto):
	html_content = "<strong>Comment to cas?</strong>"
	email = EmailMessage("my subject", html_content, "fatoni.testing@gmail.com", [emailto])
	email.content_subtype = "html"
	res = email.send()
	# res = send_mail("hello paul", "comment tu vas?", "fatoni.testing@gmail.com", 
 #         [emailto], html_message="<strong> Hello World </strong> ")
	return HttpResponse('%s' %res)

def sendEmailWithAttach(request, emailto):
	html_content = "Hello World"
	email = EmailMessage("My Subject", html_content, "fatoni.testing@gmail.com", [emailto])
	email.content_subtype = "html"

	fd = open('app1/test.html','r')
	email.attach('app1/test.html',fd.read(), 'text/plain')

	res= email.send()
	return HttpResponse('%s' %res)

class StaticView(TemplateView):
	template_name = "static.html"

def login(request):
	username = "not logged in"

	if request.method == "POST":
		MyLoginForm = LoginForm(request.POST)
		username = "POST"

		if MyLoginForm.is_valid():
			username = MyLoginForm.clean_message()
	else:
		MyLoginForm = LoginForm()

	return render(request,'loggedin.html',{"username" : username})

def SaveProfile(request):
	saved = False

	if request.method=="POST":
		MyProfileForm = ProfileForm(request.POST, request.FILES)

		if MyProfileForm.is_valid():
			profile = Profile()
			profile.name = MyProfileForm.cleaned_data["name"]
			profile.picture = MyProfileForm.cleaned_data["picture"]
			profile.save()
			saved = True

	else :
		MyProfileForm = ProfileForm()

	return render(request, 'saved.html', locals())