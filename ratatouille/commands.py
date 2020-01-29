# -*- coding: utf-8; mode: python -*-
"""
Ratatouille commands
"""

from __future__ import unicode_literals, absolute_import

import sys

from rattail import commands

from ratatouille import __version__


def main(*args):
    """
    Main entry point for Ratatouille command system
    """
    args = list(args or sys.argv[1:])
    cmd = Command()
    cmd.run(*args)


class Command(commands.Command):
    """
    Main command for Ratatouille
    """
    name = 'ratatouille'
    version = __version__
    description = "Ratatouille (custom Rattail system)"
    long_description = ''


class HelloWorld(commands.Subcommand):
    """
    The requisite 'hello world' example
    """
    name = 'hello'
    description = __doc__.strip()

    def run(self, args):
        self.stdout.write("hello world!\n")
