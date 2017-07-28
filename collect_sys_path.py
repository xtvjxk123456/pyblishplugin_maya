
import sys
import pyblish.api


class CollectSysPath(pyblish.api.ContextPlugin):
    """Inject the currently path into the Context"""

    order = pyblish.api.CollectorOrder
    label = "Current path"

    def process(self, context):
        context.data['path'] = sys.path
