# coding:utf-8
import sys
import pyblish.api
import pymel.core as pm


class CollectSceneName(pyblish.api.ContextPlugin):
    """Inject the current scene name into the Context"""

    order = pyblish.api.CollectorOrder
    label = "GetSceneName"
    # hosts = ['maya']
    host = 'maya'

    def process(self, context):
        context.data['scenename'] = pm.sceneName()
