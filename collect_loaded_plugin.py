# coding:utf-8
import pyblish.api
import pymel.core as pm
import os


class CollectLoadedPlugin(pyblish.api.ContextPlugin):
    """Collect [loadedPlugins]  Type:list"""

    order = pyblish.api.CollectorOrder
    label = "Current Loaded Plugin"
    # hosts = ['maya']
    # 只有host可以显示在pyblish qml界面上,host 可以是列表
    host = ['maya','mayapy']

    def process(self, context):
        loadedPluginPath =map(lambda x:os.path.basename(x),pm.pluginInfo(q=True,lsp=True))
        context.data['LoadedPlugins'] = loadedPluginPath
