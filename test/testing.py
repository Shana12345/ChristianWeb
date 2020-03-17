import urllib3


def test_url():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/')
    assert 200 == r.status


def test_url_About():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/About')
    assert 200 == r.status


def test_url_CreateandRecieve():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/CreateandRecieve')
    assert 200 == r.status

def test_url_EnterQuote():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/EnterQuote')
    assert 200 == r.status

def test_url_DeTrata():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.246.58.254:5000/De%20que%20se%20trata')
    assert 200 == r.status