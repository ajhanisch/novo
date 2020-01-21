# host.py

import logging
from config import Config

""" Gather novo.host module logger configuration from config.py """
log = logging.getLogger(__name__)

class Host:
    def __init__(self):
        log.critical("Host object started.")