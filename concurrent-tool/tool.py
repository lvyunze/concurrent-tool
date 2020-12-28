import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing.pool import Pool


class Multithreading(object):
    __slots__ = ['worker', 'data_list', 'thread_count']

    def __init__(self, worker, data_list, thread_count):
        self.worker = worker
        self.data_list = data_list
        self.thread_count = thread_count

    @staticmethod
    def thread_pool_callback(worker):
        pass
        # print("called thread pool executor callback function")
        # worker_exception = worker.exception()
        # if worker_exception:
        #     print("Worker return exception: {}".format(worker_exception))

    def multithreading(self):
        with ThreadPoolExecutor(self.thread_count) as executor:  # 创建 ThreadPoolExecutor
            future_list = [executor.submit(self.worker, each_appid).add_done_callback(self.thread_pool_callback)
                           for each_appid in self.data_list]  # 提交任务
        as_completed(future_list)


class Multiprocess(object):
    __slots__ = ['worker', 'data_list', 'pool_num']

    def __init__(self, worker, data_list, pool_num):
        self.worker = worker
        self.data_list = data_list
        self.pool_num = pool_num

    @staticmethod
    def process_pool_callback(worker):
        pass
        # called process pool executor callback function
        # worker_exception = worker.exception()
        # if worker_exception:
        #     print("Worker return exception: {}".format(worker_exception))

    def multiprocess(self):
        pool = Pool(self.pool_num)
        for data in self.data_list:
            pool.apply_async(self.worker, args=(data,), callback=self.process_pool_callback)
        pool.close()
        pool.join()


class Coroutines(object):
    __slots__ = ['worker_list']

    def __init__(self, worker_list: list):
        self.worker_list = worker_list

    async def task(self):
        await asyncio.gather(
            *self.worker_list
        )
    
    def run(self):
        asyncio.get_event_loop().run_until_complete(self.task)
