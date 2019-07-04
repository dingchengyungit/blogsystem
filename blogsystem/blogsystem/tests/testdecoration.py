import time
import requests


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(func.__name__, 'cost', time.time() - start)
        return result

    return wrapper


@time_it
def fetch_page():
    requests.get('http://www.baidu.com')


fetch_page()
