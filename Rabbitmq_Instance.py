# coding:utf-8
import pyblish.api
import sys
import inspect
import os


class ShowQueueMessage(pyblish.api.InstancePlugin):
    """show Message"""

    order = pyblish.api.ValidatorOrder
    label = "Log Queue Message"

    hosts = ['maya', 'mayapy', 'python']
    families = ['Rabbitmq']

    def process(self, instance):
        for index, data in enumerate(instance.data['messages']):
            self.log.info('[{}]:<Messages>:{}'.format(instance.data['queue'],

                                                      data
                                                      ))


# ----------------------------------------------------------------------------------------------------------------------
plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
