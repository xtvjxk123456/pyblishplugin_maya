# coding:utf-8
import sys
import pyblish.api
import pymel.core as pm


class CollectSceneName(pyblish.api.ContextPlugin):
    """Inject the currently path into the Context"""

    order = pyblish.api.CollectorOrder
    label = "GetSceneName"
    hosts = ['maya']

    def process(self, context):
        context.data['scenename'] = pm.sceneName()
