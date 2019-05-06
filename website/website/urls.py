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

'''urlpatterns = [
	path('time/', views.current_datetime), 
]'''

'''from django.conf.urls.defaults import *
from mysite.views import current_datetime, hours_ahead, hours_behind, now_in_chicago, now_in_london

urlpatterns = patterns('',
    ('time/', current_datetime),
    ('time/plus/(\d{1,2})/', hours_ahead),
    ('time/minus/(\d{1,2})/', hours_behind),
    ('time/in_chicago/', now_in_chicago),
    ('time/in_london/', now_in_london),
)

'''
''' 上面的url配置和下面的url配置是一样的，上面的配置的缺点是如果是导入多个函数，就要在代码前面一直导入，比较繁琐，
	下面的采用的是字符串技术，只要在url配置里面加一个参数，这样就不需要在前面导入，还有一点注意此处参数两边引号
from django.conf.urls.defaults import *

urlpatterns = patterns('website.views',
    ('time/', 'website.views.current_datetime'),
    ('time/plus/(\d{1,2})/', 'website.views.hours_ahead'),
    ('time/minus/(\d{1,2})/', 'website.views.hours_behind'),
    ('time/in_chicago/', 'website.views.now_in_chicago'),
    ('time/in_london/', 'website.views.now_in_london'),
)'''

urlpatterns = [
	path('admin/',admin.site.urls),    # django1* 的语句是(r'^admin/', include('django.contrib.admin.urls'))
	path('search/',views.search)       # 注意文件路径
]     # 该模块是管理的url模块
