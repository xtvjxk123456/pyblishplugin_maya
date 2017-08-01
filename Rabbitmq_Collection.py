# coding:utf-8
import pyblish.api
import sys
import inspect
import os
# import pika
import pyrabbit.api


def rabbitmq():
    return pyrabbit.api.Client('localhost:15672', 'guest', 'guest')


def numOfMessageInQueue(queue):
    # 这个函数需要能在线程里运行,pika是不可以的
    client = rabbitmq()
    num = client.get_queue_depth('/', queue)
    return num


class CollectRabbitmqInfo(pyblish.api.ContextPlugin):
    """create Instance"""

    order = pyblish.api.CollectorOrder + 0.2
    label = "Current Rabbitmq Infor"

    hosts = ['maya', 'mayapy', 'python']

    def process(self, context):
        try:
            temp = context.data['anipipeLocation']
        except Exception:
            self.log.error('Can not Collect Rabbitmq Infor')
        else:
            queues = rabbitmq().get_queues('/')
            context.data['publishMessageNum'] = numOfMessageInQueue('publish')
            for x in queues:
                q = context.create_instance(name='[{}],Ready:{},Unacked:{},Total:{}'.format(x['name'],
                                                                                            x['messages_ready'],
                                                                                            x[
                                                                                                'messages_unacknowledged'],
                                                                                            x['messages']))
                if x['messages']:
                    q.data['messages'] = map(lambda x: x['payload'],
                                             rabbitmq().get_messages('/', x['name'], x['messages'], True))
                else:
                    q.data['messages'] = []
                q.data['family'] = 'Rabbitmq'


plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
