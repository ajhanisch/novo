# environment.py

import logging
from config import Config

""" Gather novo.environment module logger configuration from config.py """
log = logging.getLogger(__name__)

class Environment:
    def __init__(self):
        pass

class Kvm(Environment):
    def __init__(self):
        super().__init__()
        log.debug("Kvm environment started.")