# -*- coding: utf-8; mode: python -*-
"""
Ratatouille setup script
"""

from __future__ import unicode_literals, absolute_import

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'ratatouille', '_version.py')).read())
README = open(os.path.join(here, 'README.rst')).read()


requires = [
    #
    # Version numbers within comments below have specific meanings.
    # Basically the 'low' value is a "soft low," and 'high' a "soft high."
    # In other words:
    #
    # If either a 'low' or 'high' value exists, the primary point to be
    # made about the value is that it represents the most current (stable)
    # version available for the package (assuming typical public access
    # methods) whenever this project was started and/or documented.
    # Therefore:
    #
    # If a 'low' version is present, you should know that attempts to use
    # versions of the package significantly older than the 'low' version
    # may not yield happy results.  (A "hard" high limit may or may not be
    # indicated by a true version requirement.)
    #
    # Similarly, if a 'high' version is present, and especially if this
    # project has laid dormant for a while, you may need to refactor a bit
    # when attempting to support a more recent version of the package.  (A
    # "hard" low limit should be indicated by a true version requirement
    # when a 'high' version is present.)
    #
    # In any case, developers and other users are encouraged to play
    # outside the lines with regard to these soft limits.  If bugs are
    # encountered then they should be filed as such.
    #
    # package                           # low                   high

    'psycopg2',                         # 2.6.2
    'rattail',                          # 0.7.25
    'Tailbone',                         # 0.5.29
    'pymssql',                          # 2.1.0
]


setup(
    name = "Ratatouille",
    version = __version__,
    author = "Andy Theuninck",
    author_email = "andy@gohanman.com",
    # url = "",
    description = "Rattail project for CT Integration",
    long_description = README,

    classifiers = [
        'Private :: Do Not Upload',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business',
    ],

    install_requires = requires,
    packages = find_packages(),
    include_package_data = True,

    entry_points = {

        'rattail.config.extensions': [
            'ratatouille = ratatouille.config:RatatouilleConfig',
        ],

        'console_scripts': [
            'ratatouille = ratatouille.commands:main',
        ],

        'ratatouille.commands': [
            'hello = ratatouille.commands:HelloWorld',
        ],

        'paste.app_factory': [
            'main = ratatouille.web.app:main',
        ],
    },
)
