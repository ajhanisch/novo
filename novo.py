# novo.py

import logging
import logging.config
from config import Config
from novo.host import Host
from novo.network import Network
from novo.environment import Environment

class Novo:
    """ 
    Datastructure to store results.

    _results = [
        ...
    ]
    """

    _results = None
    _blacklist = Config.NETWORK_BLACKLIST_VLAN
    _blacklist_hits = []

    def __init__(self):
        self._results = []

        for environment in args.environment:
            if environment not in self._blacklist:                
                print(environment)
            else:
                self._blacklist_hits.append(environment)

    def print_statistics(self):
        """ Print statistics about provisioned environments """

        print("Blacklist's size: {} [ filtered: {} ]".format(len(self._blacklist), len(self._blacklist_hits)))
    
if __name__ == "__main__":
    """ Parse arguments provided """
    args = Config.args

    """ Set logging configuration from config.py """
    logging.config.dictConfig(Config.LOGGING_CONFIG)

    """ Gather __main__ module logger configuration from config.py """
    log = logging.getLogger(__name__)
    
    """ Process command line """
    if args.environment:
        provisioner = Novo()

    if args.statistics:
        provisioner.print_statistics()

    """ Exit successfully """
    exit(0)