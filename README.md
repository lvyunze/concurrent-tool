> pip install concurrent-tool

> Concurrent libraries for easy use of thread pools, process pools, and coroutines

> pip install requests
```
import requests
from tool import Multithreading, Multiprocess, Coroutines

def get_info(url):
    data = requests.get(url)
    print(data.status_code)
    return data

# use multithreading

request_list = [
                "http://icanhazip.com",
                "https://github.com/OmkarPathak/pygorithm",
                "https://www.cnblogs.com/lipijin/p/3862684.html"
               ]
multithreading = Multithreading(get_info, request_list, 2)
multithreading.multithreading()

# use multiprocess
multiprocess = Multiprocess(get_info, request_list, 3)
multiprocess.multiprocess()


# use coroutines
Coroutines([get_info(url) for url in request_list])
```
