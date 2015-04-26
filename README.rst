===============
Mongo Mail Demo
===============

**Demo for** `Mongo Mail Server`_ **and** `Mongo Mail Web`_ **with no external dependencies**

- URL: http://188.165.254.60:8083
- Login: admin@example.net
- Password: password

**Include:**

- MongoDB Server
- Nginx
- `Mongo Mail Server`_
- `Mongo Mail Web`_
- Fail2ban
- Supervisor

**Disable features in Demo:**

- Change Password
- Create/Edit/Delete (User, Domain, Mynetwork, ...)

Run Demo
========

.. code:: bash

    $ git clone https://github.com/radical-software/mongo-mail-demo.git
    
    $ cd mongo-mail-demo && docker build -t mongo-mail-demo .
    
    # use --privileged for fail2ban/iptables 
    $ docker run --privileged=true -d --name mmdemo1 -p PUBLIC_IP:8083:80 mongo-mail-demo

    # For change mode and disable demo:
    $ docker run --privileged=true -d --name mmdemo1 -p PUBLIC_IP:8083:80 -e MMW_SETTINGS=mongo_mail_web.settings.Prod mongo-mail-demo
    
    # For mongodb persist use -v /home/persist/mongo-mail-demo1/db:/data/db


.. _`Mongo Mail Server`: https://github.com/radical-software/mongo-mail-server
.. _`Mongo Mail Web`: https://github.com/radical-software/mongo-mail-web
