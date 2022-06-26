from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem
from django.db import transaction
from django.db import connection


def say_hello(request):
    li = []
    return render(request, 'hello.html', {'name':'Mosh'})
