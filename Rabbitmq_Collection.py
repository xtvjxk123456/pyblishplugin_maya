# coding:utf-8
import pyblish.api
import sys
import inspect
import os
import pika


def NumOfQuene(queue):
    num = 0
    with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connect:
        with connect.channel() as channel:
            q = channel.queue_declare(queue, durable=True)
            num = q.method.message_count
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
            context.data['publishMessageNum'] = NumOfQuene('publish')
            num = context.create_instance(name='Num:{}'.format(context.data['publishMessageNum']))
            num.data['family'] = 'Rabbitmq'


plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
