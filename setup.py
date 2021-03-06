# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='mongo-mail-web-demo',
    version='0.1.1',
    description='Demo Mongo Mail',
    author='Stéphane RAULT',
    author_email='stephane.rault@radicalspam.org',
    url='https://github.com/radical-software/mongo-mail-demo',
    zip_safe=False,
    license='BSD',
    include_package_data=True,
    packages=find_packages(),
    install_requires = [
        'mongo-mail-web',
        'mongo-mail-tools',
        'mongo-mail-server',
        'supervisor',
        'gunicorn'
    ],
    dependency_links=[
      'https://github.com/radical-software/mongo-mail-web/tarball/master/#egg=mongo-mail-web-0.1.1',
      'https://github.com/radical-software/mongo-mail-tools/tarball/master/#egg=mongo-mail-tools-0.1.0',
      'https://github.com/radical-software/mongo-mail-server/tarball/master/#egg=mongo-mail-server-0.1.0'
    ],      
    test_suite='nose.collector',
    tests_require=[
      'nose',
    ],
    entry_points={
        'console_scripts': [
            'mongo-mail-web-demo = mongo_mail_web_demo.manager:main',
        ],
    },
)
