# -*- coding: utf-8 -*-

import gevent 

from mongo_mail_web import models
from mongo_mail_web import constants

def demo_task(**kwargs):
    domains = [d.name for d in models.Domain.objects]
    mynetworks = [m.ip_address for m in models.Mynetwork.objects(address_type=constants.MYNETWORK_TYPE_IP)]
    
    from mm_tools.gevent_tasks import sent_fake_mail_task
    gevent.spawn(sent_fake_mail_task, domains=domains, mynetworks=mynetworks, **kwargs)
    
