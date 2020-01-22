# config.py

import os
import logging
from argparse import ArgumentParser

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ PACKAGE VARIABLES """
    PACKAGE_NAME =         'novo'
    PACKAGE_VERSION =      '0.1.0'
    PACKAGE_AUTHOR =       'Ashton Hanisch'
    PACKAGE_AUTHOR_EMAIL = 'ajhanisch@gmail.com'
    PACKAGE_REPOSITORY =   'https://www.github.com/ajhanisch/novo'
    # PACKAGE_REPOSITORY = 'http://pypi.python.org/pypi/Novo/'
    PACKAGE_WIKI =         'https://www.github.com/ajhanisch/novo/wikis/home'

    """ PACKAGE FILES """
    FILE_LOG = os.environ.get('FILE_LOG') or \
               os.path.join(basedir, '{}.log'.format(PACKAGE_NAME))

    """ PACKAGE ARGUMENTS """
    parser = ArgumentParser(
        description="{} provides a command line interface capability to provision virtual machines on various types of hypervisors.".format(PACKAGE_NAME),
        epilog="Developed by {} ({}). Find project repository at {}. Find project wiki at {}.".format(PACKAGE_AUTHOR, PACKAGE_AUTHOR_EMAIL, PACKAGE_REPOSITORY, PACKAGE_WIKI)
    )
    parser.add_argument(
        '--id',
        nargs='+',
        metavar='0000-4094',
        required=True,
        help='id or list of environment ids to provision within specified environment'
    )
    parser.add_argument(
        '--environment',
        nargs='+',
        metavar='kvm',
        required=True,
        help='type of environment to provision with. current options are none. future options are kvm, ovirt, opennebula, vmware.'
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
        version=PACKAGE_VERSION
    )
    args = parser.parse_args()

    """ PACKAGE LOGGING """
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
                'maxBytes' : 10000000,
                'backupCount' : 5
            }
        },
        'loggers' : {
            '__main__' : {
                'handlers' : ['console', 'file'],
                'level' : 'DEBUG',
                'propogate' : False
            },
        },
    }

    """ NETWORK SETTINGS """
    NETWORK_OCTET_FIRST =    os.environ.get('NETWORK_OCTET_FIRST') or \
                             '10'
    NETWORK_OCTET_FOURTH =   os.environ.get('NETWORK_OCTET_FOURTH') or \
                             '0'
    NETWORK_DNS =            os.environ.get('NETWORK_DNS') or \
                             '1.1.1.1'
    NETWORK_SUBNET_MASK =    os.environ.get('NETWORK_SUBNET_MASK') or \
                             '255.255.255.0'
    NETWORK_GATEWAY_LAN =    os.environ.get('NETWORK_GATEWAY_LAN') or \
                             '1'
    NETWORK_GATEWAY_WAN =    os.environ.get('NETWORK_GATEWAY_WAN') or \
                             '254'
    NETWORK_BLACKLIST_VLAN = os.environ.get('NETWORK_BLACKLIST_VLAN') or \
                             [
                                 '1111',
                                 '2222'
                             ]

    """ ENVIRONMENT SETTINGS OPENNEBULA """
    ONE_API_PROTOCOL =   os.environ.get('ONE_API_PROTOCOL') or \
                         'https'
    ONE_API_HOSTNAME =   os.environ.get('ONE_API_HOSTNAME') or \
                         '192.168.90.90'
    ONE_API_PORT =       os.environ.get('ONE_API_PORT') or \
                         '2633'
    ONE_API_URI =        os.environ.get('ONE_API_URI') or \
                         'RPC2'
    ONE_API_URL =        os.environ.get('ONE_API_URL') or \
                         '{}://{}:{}/{}'.format(
                             ONE_API_PROTOCOL,
                             ONE_API_HOSTNAME,
                             ONE_API_PORT,
                             ONE_API_URI
                         )
    ONE_API_AUTH =       os.environ.get('ONE_API_AUTH') or \
                         '/var/lib/one/.one/one_auth'
    ONE_NODES =          os.environ.get('ONE_NODES') or \
                         [
                             '192.168.90.10',
                             '192.168.90.11'
                         ]
    ONE_IFCFG_LOCATION = os.environ.get('ONE_IFCFG_LOCATION') or \
                         '/etc/sysconfig/network-scripts'