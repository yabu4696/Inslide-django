from django.http import response
from django.shortcuts import render
import requests
import os
import json

# Create your views here.
def index(request):
    # params = (
    # ('fields', 'id'),
    # ('access_token', os.environ.get('ACCESS_TOKEN')),
    # )
    # response = requests.get('https://graph.instagram.com/me/media', params=params)
    # response = response.json()
    # media_id_list =[] 
    # for data in response['data']:
    #     media_id_list.append(data['id'])
    # res = bool('next' in response['paging'])
    # while bool('next' in response['paging']):
    #     url = response['paging']['next']
    #     response = requests.get(url)
    #     res = response.json()
    #     for data in res['data']:
    #         media_id_list.append(data['id'])
    # with open('/workspace/main/media_id_list.txt', mode='w') as f:
    #     for d in media_id_list:
    #         f.write(d+'\n')
    with open('/workspace/main/media_id_list.txt') as f:
        media_id_list = [s.strip() for s in f.readlines()]
    media_url_list = []
    for media_id in media_id_list:
        params = (
            ('fields', 'media_url'),
            ('access_token', os.environ.get('ACCESS_TOKEN')),
        )
        response = requests.get('https://graph.instagram.com/{}'.format(media_id), params=params)
        res = response.json()
        media_url_list.append(res['media_url'])
        # try:
        #     media_url_list.append(response['media_url'])
        # except KeyError:
        #     break
    with open('/workspace/main/media_url_list.txt', mode='w') as f:
        for d in media_url_list:
            f.write(d+'\n')
    # media_url_list = media_id_list
    return render(request, 'main/index.html',{
            'media_url_list':media_url_list,
          })