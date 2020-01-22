import logging
import logging.config
from novo import apis
from config import Config
from novo import networks
from novo import environments

def main():
    """ Parse arguments provided """
    args = Config.args

    """ Set logging configuration from config.py """
    logging.config.dictConfig(Config.LOGGING_CONFIG)

    """ Gather __main__ module logger configuration from config.py """
    log = logging.getLogger(__name__)
    
    """ Process command line """
    if 'kvm' in args.environment:
        environment = environments.KVMEnvironment()
        api = apis.KVMApi()
        network = networks.KVMNetwork()

    """ Exit successfully """
    exit(0)

if __name__ == "__main__":
    main()