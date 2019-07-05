import functools
import time

from blogsystem.tests.my_lrucache import LRUCacheDict


def cache_it(max_size=1024, expiration=60):

    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result
        return inner
    return wrapper


# def query(sql):
#     try:
#         result = CACHE[sql]
#     except KeyError:
#         time.sleep(1)
#         result = 'execute %s' % sql
#         CACHE[sql] = result
#     return result
#
#
# def query1(sql):
#     result = CACHE.get(sql)
#     if not result:
#         time.sleep(1)
#         result = 'execute %s' % sql
#         CACHE[sql] = result
#     return result


@cache_it(max_size=2, expiration=3)
def query2(sql):
    time.sleep(1)
    result = 'execute %s' % sql
    return result


if __name__ == '__main__':
    sql = 'select * from blog_post'
    start = time.time()
    query2(sql)
    print(time.time() - start)

    for i in range(20):
        start = time.time()
        query2(sql)
        print(time.time() - start)

