# coding:utf-8
import pyblish.api
import pymel.core as pm


class CollectMayaProject(pyblish.api.ContextPlugin):
    """Collect [mayaProject]"""

    order = pyblish.api.CollectorOrder
    label = "Current Maya Project"

    host = ['maya','mayapy']

    def process(self, context):
        context.data['mayaProject'] = pm.Workspace.getcwd()
