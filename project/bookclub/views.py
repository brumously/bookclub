from django.shortcuts import render
from django.http import HttpResponseRedirect
from bookclub import models
from . import forms
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request, pid=	None, del_pass=None):
	if request.user.is_authenticated: #then this should be request.aaa
		username = request.user.username
		useremail = request.user.email 
		try:
			user = auth.models.User.objects.get(username=username)
		except:
			pass
	return render(request, "bookclub/index.html", locals())

def homepage(request):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			user = auth.models.User.objects.get(username=username)
			books = models.Read.objects.filter(user=user).order_by('-date')
			tbrs = models.TBR.objects.filter(user=user).order_by('pub_time')
			asks = models.Ask.objects.filter(user=user).order_by('-pub_time')
		except:
			pass
	return render(request, "bookclub/homepage.html", locals())

def login(request):
	if request.method == 'POST':
		login_form = forms.LoginForm(request.POST)
		if login_form.is_valid():
			username = request.POST['username'].strip()
			password = request.POST['password']
			user= authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					auth.login(request, user) #if request, aaa
					messages.add_message(request, messages.SUCCESS, 'Login Success')
					return HttpResponseRedirect('/home')
				else:
					messages.add_message(request, messages.WARNING, 'Account not yet activated')
			else:
				messages.add_message(request, messages.WARNING, 'Login Failed')
		else:
			messages.add_message(request, messages.INFO, 'Please check input fields')

	else:
		login_form = forms.LoginForm()
	return render(request, 'bookclub/login.html', locals())

def logout(request):
	auth.logout(request)
	messages.add_message(request, messages.INFO, 'Logout Success')
	return HttpResponseRedirect('/')


@login_required(login_url='/bookclub/login')
def booklog(request):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			user = auth.models.User.objects.get(username=username)
			books = models.Read.objects.filter(user=user).order_by('-date')
		except:
			pass
		
	messages.get_messages(request)

	if request.method == 'POST':
		user = auth.models.User.objects.get(username = username)
		read = models.Read(user=user)
		read_form = forms.ReadForm(request.POST, instance=read) #to fill the user field not registered in diaryform
		if read_form.is_valid():
			messages.add_message(request, messages.INFO, "Saved Book Log")
			read_form.save()
			return HttpResponseRedirect('/booklog/')
		else:
			messages.add_message(request, messages.WARNING, "All fields must be filled")
	else:
		read_form=forms.ReadForm()
		messages.add_message(request, messages.WARNING, "All fields must be filled")
	return render(request, "bookclub/booklog.html", locals())

@login_required(login_url='/bookclub/login')
def viewBook(request, id):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			
			book = models.Read.objects.get(id=id)
		except:
			pass
		
	messages.get_messages(request)
	return render(request, "bookclub/viewBook.html", locals())


@login_required(login_url='/bookclub/login')
def tbr(request):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			user = auth.models.User.objects.get(username=username)
			tbrs = models.TBR.objects.filter(user=user).order_by('pub_time')
		except:
			pass
		
	messages.get_messages(request)

	if request.method == 'POST':
		user = auth.models.User.objects.get(username = username)
		tbr = models.TBR(user=user)
		tbr_form = forms.TBRForm(request.POST, instance=tbr) #to fill the user field not registered in diaryform
		if tbr_form.is_valid():
			messages.add_message(request, messages.INFO, "Saved Book To TBR List")
			tbr_form.save()
			return HttpResponseRedirect('/tbr/')
		else:
			messages.add_message(request, messages.WARNING, "All fields must be filled")
	else:
		tbr_form=forms.TBRForm()
		messages.add_message(request, messages.WARNING, "All fields must be filled")
	return render(request, "bookclub/tbr.html", locals())

@login_required(login_url='/bookclub/login')
def viewTbr(request, id):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			
			tbr = models.TBR.objects.get(id=id)
		except:
			pass
		
	messages.get_messages(request)
	return render(request, "bookclub/viewTbr.html", locals())

@login_required(login_url='/bookclub/login')
def rec(request):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			user = auth.models.User.objects.get(username=username)
			asks = models.Ask.objects.filter().order_by('-pub_time')
		except:
			pass
		
	messages.get_messages(request)

	if request.method == 'POST':
		user = auth.models.User.objects.get(username = username)
		ask = models.Ask(user=user)
		
		ask_form = forms.AskForm(request.POST, instance=ask) #to fill the user field not registered in diaryform
		if ask_form.is_valid():
			messages.add_message(request, messages.INFO, "Ask for Recommendations Submitted")
			ask_form.save()
			return HttpResponseRedirect('/ask/')
		else:
			messages.add_message(request, messages.WARNING, "All fields must be filled")
	else:
		ask_form=forms.AskForm()
		messages.add_message(request, messages.WARNING, "All fields must be filled")
	return render(request, "bookclub/rec.html", locals())

@login_required(login_url='/bookclub/login')
def viewAsk(request, id):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			ask = models.Ask.objects.get(id=id)
			recs = models.Rec.objects.filter(ask=ask).order_by('-pub_time')
		except:
			pass
		
	messages.get_messages(request)
	return render(request, "bookclub/viewAsk.html", locals())

@login_required(login_url='/bookclub/login')
def delAsk(request, id):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			ask = models.Ask.objects.get(id=id)
		except:
			ask = None
		if ask:
			ask.delete()
			messages.add_message(request, messages.SUCCESS, "Deleted Ask")
			return HttpResponseRedirect('/home/')
	#return render(request, "bookclub/homepage.html", locals())



@login_required(login_url='/bookclub/login')
def submitRec(request, id):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			ask = models.Ask.objects.get(id=id)
			#recs = models.Rec.objects.filter(ask=ask).order_by('pub_time')
		except:
			pass
		
	messages.get_messages(request)

	if request.method == 'POST':
		user = auth.models.User.objects.get(username = username)
		rec = models.Rec(user=user, ask=ask)
		rec_form = forms.RecForm(request.POST, instance=rec) #to fill the user field not registered in diaryform
		if rec_form.is_valid():
			messages.add_message(request, messages.INFO, "Submitted Recommendation")
			rec_form.save()
			return HttpResponseRedirect('')
		else:
			messages.add_message(request, messages.WARNING, "All fields must be filled")
	else:
		rec_form=forms.RecForm()
		messages.add_message(request, messages.WARNING, "All fields must be filled")
	return render(request, "bookclub/submitRec.html", locals())


@login_required(login_url='/bookclub/login')
def viewProfile(request, user):
	if request.user.is_authenticated:
		username = request.user.username
		try:
			user = auth.models.User.objects.get(username=user)
			books = models.Read.objects.filter(user=user).order_by('-date')
			tbrs = models.TBR.objects.filter(user=user).order_by('pub_time')
			asks = models.Ask.objects.filter(user=user).order_by('-pub_time')
		except:
			pass
	return render(request, "bookclub/viewProfile.html", locals())
