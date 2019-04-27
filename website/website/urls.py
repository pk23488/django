"""website URL Configuration

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
from django.contrib import admin
#from django.urls import path
#from django.conf.urls.defaults import *
from website.views import current_datetime
''',hours_ahead'''

""" 初始urlpatterns = [
    path('admin/', admin.site.urls),
]
"""   # 该初始模块其实就是管理界面的url模板
from django.urls import path
''', re_path'''

from . import views

#admin.autodiscover()

'''显示当前的时间urlpatterns = [
    path('time/', views.current_datetime),
]
'''

'''显示1-99小时后的时间，re_是正则匹配的路径
urlpatterns = [
	path('time/', views.current_datetime),
    re_path('time/plus/(\d{1,2})/', views.hours_ahead),    
]'''

'''rlpatterns = [
	path('time/', views.current_datetime), 
]'''

urlpatterns = [
	path('admin/',admin.site.urls),    # django1* 的语句是(r'^admin/', include('django.contrib.admin.urls'))
	path('search/',views.search)
]     # 该模块是管理的url模块
