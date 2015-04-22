# -*- coding: utf-8 -*-

from decouple import config as config_from_env

from mongo_mail_web.wsgi import create_app as base_create_app
from mongo_mail_web import models
from mongo_mail_web import constants

from . import tasks

def _patch_admin(app):
    admin = app.extensions['admin'][0]
    from mongo_mail_web.admin import UserModelView, DomainView, MynetworkView, TransportView
    model_views = (UserModelView, DomainView, MynetworkView, TransportView)
    for m in admin._views:
        if isinstance(m, model_views):
            m.can_edit = False
            m.can_create = False
            m.can_delete = False
            if not m.action_disallowed_list:
                m.action_disallowed_list = []
            if not 'delete' in m.action_disallowed_list:
                m.action_disallowed_list.append('delete')
        if isinstance(m, UserModelView):
            m.form_excluded_columns = ('password',)
    
def _configure_demo(app):
    
    @app.before_first_request
    def reset():
        models.User.drop_collection()
        models.User.create_user(username=config_from_env('MMW_SUPERADMIN_EMAIL', 'admin@example.net'), 
                                password=config_from_env('MMW_SUPERADMIN_PASSWORD', 'password'), 
                                role="superadmin", 
                                group=constants.GROUP_DEFAULT)
        
        for i in xrange(1, 10):
            models.Domain.objects.get_or_create(name="example-%s.net" % i)
            models.Mynetwork.objects.get_or_create(ip_address="10.0.0.%d" % i)

def create_app(config='mongo_mail_web_demo.settings.Demo'):
    app = base_create_app(config=config)
    _patch_admin(app)
    _configure_demo(app)
    tasks.demo_task(**app.config.get('TASK_DEMO_SETTINGS'))
    return app
