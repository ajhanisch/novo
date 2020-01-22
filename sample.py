import logging
import logging.config
from novo import apis
from novo import hosts
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
        for id in args.id:
            wan = networks.BaseNetwork(
                vlan=str(id), 
                octet_first=Config.NETWORK_OCTET_FIRST, 
                octet_fourth=Config.NETWORK_OCTET_FOURTH, 
                dns=Config.NETWORK_DNS, 
                subnet_mask=Config.NETWORK_SUBNET_MASK, 
                gateway=Config.NETWORK_GATEWAY_WAN
            )
            print(wan)

            lan = networks.BaseNetwork(
                vlan=format(int(id) + 1, '004d'), 
                octet_first=Config.NETWORK_OCTET_FIRST, 
                octet_fourth=Config.NETWORK_OCTET_FOURTH, 
                dns=Config.NETWORK_DNS, 
                subnet_mask=Config.NETWORK_SUBNET_MASK, 
                gateway=Config.NETWORK_GATEWAY_LAN
            )
            print(lan)

    """ Exit successfully """
    exit(0)

if __name__ == "__main__":
    main()