
"""
Command-line interface to the Smart Data.
"""

import argparse
import os
import sys

from smartdata import utils
from smartdata.v1_0 import shell as shell_v1_0


def env(*vars, **kwargs):
    """Search for the first defined of possibly many env vars

    Returns the first environment variable defined in vars, or
    returns the default defined in kwargs.

    """
    for v in vars:
        value = os.environ.get(v, None)
        if value:
            return value
    return kwargs.get('default', '')


class SmartDataShell(object):

    def get_base_parser(self):
        parser = argparse.ArgumentParser(
            prog='smartdata',
            description=__doc__.strip(),
            epilog='See "smartdata help COMMAND" '
                   'for help on a specific command.',
            add_help=False,
            formatter_class=SmartDataHelpFormatter,
        )

        # Global arguments
        parser.add_argument('-h',
                            '--help',
                            action='store_true',
                            help=argparse.SUPPRESS)

        parser.add_argument('--debug',
                            default=False,
                            action='store_true',
                            help=argparse.SUPPRESS)
        return parser

    def get_subcommand_parser(self, version):
        parser = self.get_base_parser()
        self.subcommands = {}
        subparsers = parser.add_subparsers(metavar='<subcommand>')
        try:
            actions_module = {
                '1.0': shell_v1_0,
            }[version]
        except KeyError:
            actions_module = shell_v1_0
        self._find_actions(subparsers, actions_module)
        self._find_actions(subparsers, self)

        return parser

    def _find_actions(self, subparsers, actions_module):
        for attr in (a for a in dir(actions_module) if a.startswith('do_')):
            # I prefer to be hypen-separated instead of underscores.
            command = attr[3:].replace('_', '-')
            callback = getattr(actions_module, attr)
            desc = callback.__doc__ or ''
            help = desc.strip().split('\n')[0]
            arguments = getattr(callback, 'arguments', [])
            subparser = subparsers.add_parser(
                command,
                help=help,
                description=desc,
                add_help=False,
                formatter_class=SmartDataHelpFormatter)
            subparser.add_argument('-h', '--help', action='help',
                                   help=argparse.SUPPRESS)
            self.subcommands[command] = subparser
            for (args, kwargs) in arguments:
                subparser.add_argument(*args, **kwargs)
            subparser.set_defaults(func=callback)

    def main(self, argv):
        # Parse args once to find version
        parser = self.get_base_parser()
        (options, args) = parser.parse_known_args(argv)

        subcommand_parser = self.get_subcommand_parser('1.0')
        self.parser = subcommand_parser
        # Handle top-level --help/-h before attempting to parse
        # a command off the command line
        if not argv or options.help:
            self.do_help(options)
            return 0

        # Parse args again and call whatever callback was selected
        args = subcommand_parser.parse_args(argv)
        args.func(args)
        # Short-circuit and deal with help command right away.
        if args.func == self.do_help:
            self.do_help(args)
            return 0

    @utils.arg('command', metavar='<subcommand>', nargs='?',
                          help='Display help for <subcommand>')
    def do_help(self, args):
        """
        Display help about this program or one of its subcommands.
        """
        if getattr(args, 'command', None):
            if args.command in self.subcommands:
                self.subcommands[args.command].print_help()
            else:
                raise Exception("'%s' is not a valid subcommand" %
                                       args.command)
        else:
            self.parser.print_help()


# I'm picky about my shell help.
class SmartDataHelpFormatter(argparse.HelpFormatter):
    def start_section(self, heading):
        # Title-case the headings
        heading = '%s%s' % (heading[0].upper(), heading[1:])
        super(SmartDataHelpFormatter, self).start_section(heading)


def main():
    try:
        SmartDataShell().main(sys.argv[1:])
    except Exception, e:
        print >> sys.stderr, e
        sys.exit(0)