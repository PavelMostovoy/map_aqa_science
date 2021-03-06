"""aqa_science URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.gis import admin, apps
from django.urls import include, path
from init_map.views import home, \
    map_representation, \
    location, \
    main_page, \
    add_item, \
    save_user_geolocation

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^map/', map_representation),
    url(r'^location/', location, name='location'),
    url(r'^$', main_page,name='Home'),
    url(r'^add/',add_item,name='Add Item'),
    url(r'^coords', save_user_geolocation, name='Receive Coord'),
]