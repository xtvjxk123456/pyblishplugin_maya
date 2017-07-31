# coding:utf-8
import sys
import pyblish.api


class CollectPythonPath(pyblish.api.ContextPlugin):
    """Collect [pythonPath]"""

    order = pyblish.api.CollectorOrder
    label = "Current Python Sys Path"
    # hosts = ['maya']
    # 只有host可以显示在pyblish qml界面上,host 可以是列表
    host = ['maya', 'mayapy']

    def process(self, context):
        context.data['pythonPath'] = sys.path
