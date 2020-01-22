# sample.py

import logging
import novo.api
import novo.host
import novo.network
import logging.config
import novo.environment
from config import Config

def main():
    """ Parse arguments provided """
    args = Config.args

    """ Set logging configuration from config.py """
    logging.config.dictConfig(Config.LOGGING_CONFIG)

    """ Gather __main__ module logger configuration from config.py """
    log = logging.getLogger(__name__)
    
    """ Process command line """
    if 'kvm' in args.environment:
        environment = novo.environment.Kvm()
        api = novo.api.Kvm()
        network = novo.network.Kvm()
        host = novo.host.Kvm()

    """ Exit successfully """
    exit(0)

if __name__ == "__main__":
    main()