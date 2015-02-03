from django.conf.urls import patterns, include, url
from django.contrib import admin
#from details.views import Student_Form,contacts_hello
from details.views import contacts_hello,Student_Form

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts_hello/',contacts_hello),
    url(r'^Student_Form/',Student_Form),
)

