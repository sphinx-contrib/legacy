# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

f = open('README', 'r')
try:
    long_desc = f.read()
finally:
    f.close()

requires = ['Sphinx>=0.6',
            'SQLAlchemy',
            ]

setup(
    name='sphinxcontrib-sqltable',
    version='1.0',
    url='http://bitbucket.org/birkenfeld/sphinx-contrib',
    license='BSD',
    author='Doug Hellmann',
    author_email='doug.hellmann@gmail.com',
    description='Sphinx "SQLTable" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
