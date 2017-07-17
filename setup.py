#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='filetype',
    version='0.1.5',
    description='Infer file type and MIME type of any file/buffer. '
                'No libmagic dependency.',
    long_description=open('README.rst').read(),
    keywords='file libmagic magic infer numbers magicnumbers discovery mime '
             'type kind',
    url='https://github.com/h2non/filetype.py',
    download_url='https://github.com/h2non/filetype.py/tarball/master',
    author='Tomas Aparicio',
    author_email='tomas@aparicio.me',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'],
    platforms=['any'],
    packages=find_packages(exclude=['dist', 'build', 'docs', 'tests']),
    package_data={'filetype': ['LICENSE', '*.md']},
    zip_safe=True)
