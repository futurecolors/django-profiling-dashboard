#!/usr/bin/env python
from setuptools import setup

version = '1.0'

setup(
    name='django-profiling-dashboard-fc',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['profiling_dashboard'],
    package_data={
        'profiling_dashboard': ['templates/profiling_dashboard/*.html', ]
    },

    url='https://github.com/kmike/django-profiling-dashboard',
    download_url='https://github.com/kmike/django-profiling-dashboard/zipball/master',
    license='MIT license',
    description=""" Django profiling dashboard for debugging CPU, memory and other resources usage in live servers """,

    long_description=open('README.rst').read(),
    install_requires=[
        'django>=1.3',
        'yappi==0.62',
        'psutil==0.7.0',
        'pympler==0.3.1',
        'django-query-exchange-fc==1.0'],

    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
