# coding:utf-8
import sys
import pyblish.api
import pymel.core as pm


class CollectSceneName(pyblish.api.ContextPlugin):
    """Inject the current scene name into the Context"""

    order = pyblish.api.CollectorOrder
    label = "GetSceneName"
    # hosts = ['maya']
    # 只有host可以显示在pyblish qml界面上,host 可以是列表
    host = 'maya'

    def process(self, context):
        context.data['scenename'] = pm.sceneName()
