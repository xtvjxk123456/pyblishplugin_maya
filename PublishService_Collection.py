# coding:utf-8
import pyblish.api
import win32serviceutil


class CollectPublishService(pyblish.api.ContextPlugin):
    """create service Instance"""
    order = pyblish.api.CollectorOrder +0.2
    label = "Current PublishService Infor"

    hosts = ['maya', 'mayapy', 'python']

    def process(self, context):
        try:
            status = win32serviceutil.QueryServiceStatus('AniPipePublisher')
        except Exception:
            self.log.error('AniPipePubilsher do not Exist!')
        else:
            runStatus = status[1]
            info = {'1': 'Stopped', '4': 'Running'}
            instance = context.create_instance(name='AniPipePublisher')
            instance.data['family'] = 'PublishService'
            instance.data['status'] = info.setdefault(str(runStatus), 'UnKnown')
