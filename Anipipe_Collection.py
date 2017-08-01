# coding:utf-8
import pyblish.api
import sys
import inspect
import os


class CollectAnipipeInfo(pyblish.api.ContextPlugin):
    """create Instance"""

    order = pyblish.api.CollectorOrder
    label = "Current Anipipe Infor"

    hosts = ['maya', 'mayapy', 'python']

    def process(self, context):
        try:
            anipipeTool = os.environ['ANIPIPE_TOOLS_LOC']
        except Exception:
            self.log.error('ANIPIPE_TOOLS_LOC has not been setted!')
        else:
            context.data['anipipeLocation']= anipipeTool
            tool = context.create_instance(name=context.data['anipipeLocation'])
            tool.data['family'] = 'Anipipe'
            tool.data['icon'] = 'bus'





plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
