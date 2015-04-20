#!/bin/bash

echo "--> start.sh script running..."

exec /usr/local/bin/supervisord --nodaemon -c /etc/supervisor/supervisord.conf
