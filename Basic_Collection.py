# coding:utf-8
import pyblish.api
import pymel.core as pm
import sys
import inspect
import os

# 事实证明一个文件内写多个plugin是可以的,
# hosts才是对的
# pyblish_qml启动的时候的host是python
# 想要使用自己的plugin需要注册host

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
        if os.path.exists(context.data['mayaSceneName']):
            filename =context.create_instance(name=os.path.basename(context.data['mayaSceneName']))
            filename.data['family'] = ['Scene']
            filename.data['icon'] = 'tint'


# -------------------------------------------------------------------------------------------
# 检索模块
plugins = []
for x, y in locals().items():
    if inspect.isclass(y):
        plugins.append(y)
