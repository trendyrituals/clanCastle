from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from .models import Course, Coin
from .forms import CourseForm
# Create your views here.
def home(request):
	if request.user.is_authenticated():
		user = request.user
		email = request.user.email
		course_count = Course.objects.filter(user_name=request.user).count()
		context = {
		"user": user,
		"email": email,
		"course_count": course_count
		}
		return render(request,"user_dash.html", context)

def search_course(request):
	if request.user.is_authenticated():
		return render(request,"search_course.html")

def user_course(request):
	if request.user.is_authenticated():
		course_list = Course.objects.filter(user_name = request.user).order_by("-id")
		context = {
		"object_list": course_list
		}
		return render(request,"user_course.html", context)


# user add course view or function 

def add_course(request):
	if request.user.is_authenticated():
		form = CourseForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			new_course = form.save(commit=False)
			new_course.user_name = request.user
			new_course.save()
			get_coin = Coin.objects.get(user_name=request.user)
			coin_usr = get_coin.coin+1
			get_coin.coin = coin_usr
			get_coin.save()
			form = CourseForm()
		context = {
		"form": form
		}
		return render(request,"add_course.html", context)





def user_course_view(request, id=None):
	instance = get_object_or_404(Course, id=id)
	context = {
		"title" : instance.course_name,
		"instance": instance,
		"subject" : instance.subject,
		"description" : instance.description,
	}
	return render(request, "course_view.html", context)





def coins(request):
	if request.user.is_authenticated():
		return render(request,"coin.html")


def account_summary(request):
	if request.user.is_authenticated():
		return render(request,"account_summary.html")


def profile(request):
	if request.user.is_authenticated():
		return render(request,"profile.html")


def logout_view(request):
	logout(request)
	return redirect("/")