# config.py

import os
import logging
from argparse import ArgumentParser

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ MODULE VARIABLES """
    MODULE_NAME =         'novo'
    MODULE_VERSION =      '0.1'
    MODULE_AUTHOR =       'Ashton Hanisch'
    MODULE_AUTHOR_EMAIL = 'ajhanisch@gmail.com'
    MODULE_REPOSITORY =   'https://www.github.com/ajhanisch/novo'
    MODULE_WIKI =         'https://www.github.com/ajhanisch/novo/wikis/home'

    """ MODULE FILES """
    FILE_LOG = os.environ.get('FILE_LOG') or \
               os.path.join(basedir, 'novo.log')

    """ MODULE ARGUMENTS """
    parser = ArgumentParser(
        description="{} performs provisioning tasks for various hypervisors. (Compatible with none currently.)".format(MODULE_NAME),
        epilog="Developed by {} ({}). Find project repository at {}. Find project wiki at {}.".format(MODULE_AUTHOR, MODULE_AUTHOR_EMAIL, MODULE_REPOSITORY, MODULE_WIKI)
    )
    parser.add_argument(
        '--environment',
        nargs='+',
        metavar='1234',
        required=True,
        help='environment or list of environments to provision'

    )
    parser.add_argument(
        '--statistics',
        action='store_true',
        default=False,
        help='Print statistics about provisioned environments'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,
        help='increase verbosity levels (-v, -vv, ...)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version=MODULE_VERSION
    )
    args = parser.parse_args()

    """ MODULE LOGGING """
    LOGGING_LEVELS = [
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG
    ]
    LOGGING_LEVEL = LOGGING_LEVELS[min(len(LOGGING_LEVELS)-1, args.verbose)]
    LOGGING_CONFIG = {
        'version' : 1,
        'disable_existing_loggers' : True,
        'formatters' : {
            'default' : {
                'format' :  '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers' : {
            'console' : {
                'level' : LOGGING_LEVEL,
                'class' : 'logging.StreamHandler',
                'formatter' : 'default',
                'stream' : 'ext://sys.stdout'
            },
            'file' : {
                'level' : 'DEBUG',
                'class' : 'logging.handlers.RotatingFileHandler',
                'formatter' : 'default',
                'filename' : FILE_LOG,
                'maxBytes' : 1024,
                'backupCount' : 5
            }
        },
        'loggers' : {
            'default' : {
                'level' : 'WARNING',
                'handlers' : ['console', 'file']
            },
            '__main__' : {
                'handlers' : ['console', 'file'],
                'level' : LOGGING_LEVEL,
                'propogate' : False
            },
            'novo.environment' : {
                'level' : LOGGING_LEVEL,
                'handlers' : ['console', 'file'],
                'propogate' : False
            },
            'novo.network' : {
                'level' : LOGGING_LEVEL,
                'handlers' : ['console', 'file'],
                'propogate' : False
            },
            'novo.host' : {
                'level' : LOGGING_LEVEL,
                'handlers' : ['console', 'file'],
                'propogate' : False
            },
        }
    }

    """ NETWORK SETTINGS """
    NETWORK_OCTET_FIRST =    os.environ.get('NETWORK_OCTET_FIRST') or \
                             '10'
    NETWORK_OCTET_LAST =     os.environ.get('NETWORK_OCTET_LAST') or \
                             '0'
    NETWORK_DNS =            os.environ.get('NETWORK_DNS') or \
                             '1.1.1.1'
    NETWORK_SUBNET_MASK =    os.environ.get('NETWORK_SUBNET_MASK') or \
                             '255.255.255.0'
    NETWORK_GATEWAY_LAN =    os.environ.get('NETWORK_GATEWAY_LAN') or \
                             '1'
    NETWORK_GATEWAY_WAN =    os.environ.get('NETWORK_GATEWAY_WAN') or \
                             '254'
    NETWORK_BLACKLIST_VLAN = [
        '1111',
        '2222'
    ]

    """ ENVIRONMENT SETTINGS OPENNEBULA """
    ONE_API_PROTOCOL = os.environ.get('ONE_API_PROTOCOL') or \
                       'https'
    ONE_API_HOSTNAME = os.environ.get('ONE_API_HOSTNAME') or \
                       '192.168.90.90'
    ONE_API_PORT =     os.environ.get('ONE_API_PORT') or \
                       '2633'
    ONE_API_URI =      os.environ.get('ONE_API_URI') or \
                       'RPC2'
    ONE_API_AUTH =     os.environ.get('ONE_API_AUTH') or \
                       '/var/lib/one/.one/one_auth'
    ONE_NODES =        os.environ.get('ONE_NODES') or \
                       [
                           '192.168.90.10',
                           '192.168.90.11'
                       ]