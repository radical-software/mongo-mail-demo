# -*- coding: utf-8 -*-

from mongo_mail_web.manager import main as base_main

def main():
    from mongo_mail_web_demo.wsgi import create_app
    base_main(create_app_func=create_app)

if __name__ == "__main__":
    """
    python -m mongo_mail_web_demo.manager -c mongo_mail_web_demo.settings.Demo config
    mongo-mail-web-demo -c mongo_mail_web_demo.settings.Demo server
    """
    main()
