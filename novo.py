# novo.py

import logging
import logging.config
from config import Config
from novo.host import Host
from novo.network import Network
from novo.environment import Environment, Kvm

class Novo:
    """ 
    Datastructure to store results.

    _results = {
        kvm: [ info, host_1, host_N ]
        ...
        environment_N: ...
    }

    info = {
        ...
    }

    host = {
        ...
    }
    """

    _results = None
    _blacklist = Config.NETWORK_BLACKLIST_VLAN
    _blacklist_hits = []

    def __init__(self):
        self._results = {}

    def environment(self, environment):
        if environment == 'kvm':
            self.environment = Kvm()

        return self.environment
        
    def network(self):
        return Network()

    def hosts(self):
        return Host()
    
if __name__ == "__main__":
    """ Parse arguments provided """
    args = Config.args

    """ Set logging configuration from config.py """
    logging.config.dictConfig(Config.LOGGING_CONFIG)

    """ Gather __main__ module logger configuration from config.py """
    log = logging.getLogger(__name__)
    
    """ Process command line """
    if args.environment and args.id:
        for env in args.environment:
            provisioner = Novo()
            environment = provisioner.environment(environment=env)
            network = provisioner.network()
            hosts = provisioner.hosts()

    """ Exit successfully """
    exit(0)