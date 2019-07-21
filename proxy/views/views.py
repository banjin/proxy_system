from django.shortcuts import render
from utils import getter,redis_client
from django.http import HttpResponse, JsonResponse


redisdb = redis_client.RedisClient()

def proxy(request):
    return redisdb.get_proxy()

def proxy_num(request):
    return redisdb.get_proxy_count()