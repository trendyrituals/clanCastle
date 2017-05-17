from django.conf.urls import url
from .views import (
		home,
		add_course,
		coins,
		profile,
		logout_view,
		account_summary,
		search_course,
		user_course,
		user_course_view	
	)


urlpatterns = [
	url(r'^user_course/(?P<id>\d+)/$', user_course_view, name='user_course_view'),
	url(r'^user_course/$', user_course, name='user_course'),
	url(r'^search/$', search_course, name='search_course'),
	url(r'^summary/$', account_summary, name='account_summary'),
    url(r'^logout/$', logout_view, name='logout_view'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^coins/$', coins, name='coins'),
    url(r'^add_course/$', add_course, name='add_course'),
    url(r'^$', home, name='home'),
    ]
