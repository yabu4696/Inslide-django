from django.http import response
from django.shortcuts import render
import requests
import os
import json
import random

def index(request):
    return render(request, 'main/index.html')

def slide(request):
    with open('/workspace/main/media_url_list_copy.txt') as f:
        media_url_list = [s.strip() for s in f.readlines()]
    random.shuffle(media_url_list)
    return render(request, 'main/slide.html',{
            'media_url_list':media_url_list,
          })
def get_id(request):
    params = (
    ('fields', 'id'),
    ('access_token', os.environ.get('ACCESS_TOKEN')),
    )
    response = requests.get('https://graph.instagram.com/me/media', params=params)
    res = response.json()
    media_id_list =[] 
    for data in res['data']:
        media_id_list.append(data['id'])
    while bool('next' in res['paging']):
        url = res['paging']['next']
        response = requests.get(url)
        res = response.json()
        for data in res['data']:
            media_id_list.append(data['id'])
    with open('/workspace/main/media_id_list.txt', mode='w') as f:
        for d in media_id_list:
            f.write(d+'\n')
    return render(request, 'main/done.html')

def get_url(request):
    with open('/workspace/main/media_id_list_copy.txt') as f:
        media_id_list = [s.strip() for s in f.readlines()]
    with open('/workspace/main/media_url_list_copy.txt') as f:
        media_url_list = [s.strip() for s in f.readlines()]
    media_id_list = media_id_list[len(media_url_list):]
    media_url_list = []
    for media_id in media_id_list:
        params = (
            ('fields', 'media_url'),
            ('access_token', os.environ.get('ACCESS_TOKEN')),
        )
        response = requests.get('https://graph.instagram.com/{}'.format(media_id), params=params)
        res = response.json()
        try:
            media_url_list.append(res['media_url'])
        except KeyError:
            break
    with open('/workspace/main/media_url_list_copy.txt', mode='a') as f:
        for d in media_url_list:
            f.write(d+'\n')
    return render(request, 'main/done.html')