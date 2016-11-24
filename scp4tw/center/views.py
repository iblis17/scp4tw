from django.http import HttpResponse
from django.shortcuts import render

import opencc
import requests


def index(request):
    return render(request, 'base.html')


def opencc_view(request, id):
    url = 'http://scp-wiki-cn.wikidot.com/scp-{}'.format(id)
    res = requests.get(url)

    if res.status_code != 200:
        return

    html = opencc.convert(res.text, config='s2tw.json')

    return HttpResponse(html)
