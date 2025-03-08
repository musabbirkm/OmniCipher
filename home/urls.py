from django.urls import path
from home import views
from django.contrib import admin

admin.site.site_headern = "Admin Pannel"
admin.site.site_title = "Welcome to OminiCipher Dashboard"
admin.site.index_title = "Welcome"

urlpatterns = [
    path('',views.index,name='home'),
    path('home/',views.index,name='home'),
    path('contact/',views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("services",views.services,name="services"),
    path("projects/",views.projects,name="projects"),
    path("blogs/",views.blogs,name="blogs"),
    path("blog1/",views.blog1,name="blog1"),
    path("blog2/",views.blog2,name="blog2"),
    path("blog3/",views.blog3,name="blog3"),
    path("blog4/",views.blog4,name="blog4"),
    path("blog5/",views.blog5,name="blog5"),
    path("blog6/",views.blog6,name="blog6"),
    path("blog7/",views.blog7,name="blog7"),
    path("blog8/",views.blog8,name="blog8"),
]