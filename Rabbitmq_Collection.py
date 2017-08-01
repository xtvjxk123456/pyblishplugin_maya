# coding:utf-8
import pyblish.api
import sys
import inspect
import os
import pika


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
            pass
            # 这里不好操作


plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
