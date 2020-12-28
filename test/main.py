from tool import Multithreading, Multiprocess, Coroutines
import unittest
from request import get_info


class TestTool(unittest.TestCase):
    def test_multithreading(self):
        request_list = ["http://icanhazip.com",
                        "https://github.com/OmkarPathak/pygorithm",
                        "https://www.cnblogs.com/lipijin/p/3862684.html"]
        multithreading = Multithreading(get_info, request_list, 2)
        multithreading.multithreading()

    def test_multiprocess(self):
        request_list = ["http://icanhazip.com",
                        "https://github.com/OmkarPathak/pygorithm",
                        "https://www.cnblogs.com/lipijin/p/3862684.html"]
        multiprocess = Multiprocess(get_info, request_list, 3)
        multiprocess.multiprocess()

    def test_coroutines(self):
        request_list = ["http://icanhazip.com",
                        "https://github.com/OmkarPathak/pygorithm",
                        "https://www.cnblogs.com/lipijin/p/3862684.html"]

        Coroutines([get_info(url) for url in request_list])


if __name__ == '__main__':
    unittest.main()



