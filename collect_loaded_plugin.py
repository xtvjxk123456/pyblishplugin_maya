# coding:utf-8
import pyblish.api
import pymel.core as pm


class CollectLoadedPlugin(pyblish.api.ContextPlugin):
    """Collect [loadedPlugins]  Type:list"""

    order = pyblish.api.CollectorOrder
    label = "Current Loaded Plugin"
    # hosts = ['maya']
    # 只有host可以显示在pyblish qml界面上,host 可以是列表
    hosts = ['maya','mayapy']

    def process(self, context):
        loadedPluginPath =map(lambda x:pm.Path(x).basename().name,pm.pluginInfo(q=True,lsp=True))
        context.data['LoadedPlugins'] = loadedPluginPath
        # self.log.info('current pyblish_qml host is {}'.format(pyblish.api.current_host()))
