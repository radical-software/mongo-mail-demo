# -*- coding: utf-8 -*-

from decouple import config

from mongo_mail_web.settings import Config

class Demo(Config):

    DEMO_MODE = True

    MAIL_SUPPRESS_SEND = True
    
    SECURITY_CHANGEABLE = False
    SECURITY_RECOVERABLE = False
    
    TASK_DEMO_SETTINGS = dict(host=config('MMW_DEMO_MMS_HOST', '127.0.0.1'), 
                              port=config('MMW_DEMO_MMS_PORT', 14001, cast=int), 
                              xforward_enable=True,
                              period=5,
                              message_per_step=2,
                              vary_message_type=True,
                              random_files=1,
                              smtp_timeout=10,
                              stop_with_error=False)    
    
