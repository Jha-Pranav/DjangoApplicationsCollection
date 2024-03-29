"""PersonalOpenSorceApplications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from Pool.views import index


urlpatterns = [
    path('', include('OfficialBlogPost.urls')),
    path('pool/', include('Pool.urls')),
    path('admin/', admin.site.urls),
    path('account/login', views.LoginView.as_view(), name='login'),
    path('account/logout', views.LogoutView.as_view(),name='logout', kwargs={'nextpage': '/'}),
 
]

# # default: "Django Administration"
# admin.site.site_header = 'Project Admin'
# # default: "Site administration"
# admin.site.index_title = 'Features area'
# # default: "Django site admin"
# admin.site.site_title = 'HTML title from adminsitration'
