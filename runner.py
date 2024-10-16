from urllib import request,parse, error
from lgtm import core
from tests import test_core

import requests
import json
import greet



if __name__ == "__main__": 
    
    query = parse.urlencode({'q': 'python'})

    # httpbin은 요청 내용을 반환해 줌
    url = f'https://httpbin.org/get?{query}'
    try:
        with request.urlopen(url) as f:
            res = f.read().decode('utf-8')
    except error.HTTPError as e:
        print(e)

    json.loads(res)

    res = requests.get('https://httpbin.org/get',
                   params={'q': 'python'})
    res.json()

    res = requests.post('https://httpbin.org/post',
                    data={'q': 'python'})
    #print(res.json().keys())
    #print(res.json()['form'])

    core.cli()
   
    