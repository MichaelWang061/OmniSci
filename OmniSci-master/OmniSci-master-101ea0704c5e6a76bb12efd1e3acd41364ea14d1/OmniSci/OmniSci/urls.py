"""OmniSci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

import FunctionPage.views as fv
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include
from Project.views import MySearchView
from Project.views import Search
from FunctionPage.views import contact_address
from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'home/',  include(("Home.urls", "Home"), namespace="Home")),
    path(r'user/',  include(("User.urls", "User"), namespace="User")),
    path(r'template/', include(("PageTemplate.urls", "PageTemplate"), namespace="PageTemplate")),
    path(r'favicon.ico', RedirectView.as_view(url='static/images/ico/source.ico')),
    path(r'project/', include(("Project.urls", "Project"), namespace="Project")),
    #path(r'search/', MySearchView(), name='haystack_search'),
    #path(r'search/', include(("Search.urls", "Search"), namespace="Search")),
    path(r'search/', Search),
    path(r'contact/', fv.contact, name='contact'),
    path(r'contact/<str:link>/', contact_address)
]
