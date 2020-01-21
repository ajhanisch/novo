# network.py

import logging
from config import Config

""" Gather novo.network module logger configuration from config.py """
log = logging.getLogger(__name__)

class Network:
    def __init__(self):
        log.error("Network object started.")