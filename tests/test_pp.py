import requests
def test_home():
    r = requests.get("http://140.137.218.51:5001?a= &b=1")
    assert r.status_code == 200