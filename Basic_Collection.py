# coding:utf-8
import pyblish.api
import pymel.core as pm
import sys
import inspect


class CollectLoadedPlugin(pyblish.api.ContextPlugin):
    """Collect [loadedPlugins]  Type:list"""

    order = pyblish.api.CollectorOrder
    label = "Current Loaded Plugin"
    # hosts = ['maya']
    # 只有host可以显示在pyblish qml界面上,host 可以是列表
    # 这是因为在maya里运行的时候,本质pyblish_qml的host是python
    # 需要手动注册,不能使用环境变量方式
    hosts = ['maya', 'mayapy']

    def process(self, context):
        loadedPluginPath = map(lambda x: pm.Path(x).basename().name, pm.pluginInfo(q=True, lsp=True))
        context.data['LoadedPlugins'] = loadedPluginPath


class CollectMayaProject(pyblish.api.ContextPlugin):
    """Collect [mayaProject]"""

    order = pyblish.api.CollectorOrder
    label = "Current Maya Project"

    hosts = ['maya', 'mayapy']

    def process(self, context):
        context.data['mayaProject'] = pm.Workspace.getcwd()


class CollectPythonPath(pyblish.api.ContextPlugin):
    """Collect [pythonPaths] Type:list"""

    order = pyblish.api.CollectorOrder
    label = "Current Python Sys Path"

    hosts = ['maya', 'mayapy']

    def process(self, context):
        context.data['pythonPaths'] = sys.path


class CollectSceneName(pyblish.api.ContextPlugin):
    """Collect [mayaSceneName]"""

    order = pyblish.api.CollectorOrder
    label = "Current Maya Scene"

    hosts = ['maya', 'mayapy']

    def process(self, context):
        context.data['mayaSceneName'] = pm.sceneName()


# 检索模块
plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
