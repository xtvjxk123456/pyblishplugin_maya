# coding:utf-8
import sys
import pyblish.api
import pymel.core as pm


class CollectSceneName(pyblish.api.ContextPlugin):
    """Collect [mayaSceneName]"""

    order = pyblish.api.CollectorOrder
    label = "Current Maya Scene"
    # hosts = ['maya']
    # 只有host可以显示在pyblish qml界面上,host 可以是列表
    host = ['maya','mayapy']

    def process(self, context):
        context.data['mayaSceneName'] = pm.sceneName()
