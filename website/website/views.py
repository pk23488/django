#!/usr/bin/env python
# 视图函数的作用就是把模板装载到显示的页面
'''from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>亲爱的南邮吴亦凡：It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>亲爱的南邮吴亦凡：In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)'''
from django.template.loader import get_template
# from django.template import Context
from django.http import HttpResponse
import datetime

'''def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render({'current_date': now})    # 在django1.1是html = t.render(Content({'current_date': now}))  
    return HttpResponse(html)'''
	
# 上面定义的函数可以简化，利用django中的一个函数 render_to_response()
from django.shortcuts import render_to_response
from django.db.models import Q
from books.models import Book
from django.apps.forms import ContactForm

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('dateapp/current_datetime.html', {'current_date': now})   # 此时的第一个参数改变成'dateapp/current_datetime.html'，是因为我重新把模板存放于模板目录的子目录中，这会让模板的文件夹看起来更规范


	
# 相比上面的三行代码，代码易读性提高了一点,但是准确性没有上一个好，因为locals（）是包含了该函数中所有变量的键值对
'''def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())'''

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })

