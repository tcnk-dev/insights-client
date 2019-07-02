#!/usr/bin/env python
"""
 Gather and upload Insights data for
 Red Hat Insights
"""
from __future__ import print_function
import os
import sys
import subprocess
from subprocess import PIPE
import shlex
import logging
import logging.handlers

GPG_KEY = "/etc/insights-client/redhattools.pub.gpg"

BYPASS_GPG = os.environ.get("BYPASS_GPG", "").lower() == "true"
ENV_EGG = os.environ.get("EGG")
NEW_EGG = "/var/lib/insights/newest.egg"
STABLE_EGG = "/var/lib/insights/last_stable.egg"
RPM_EGG = "/etc/insights-client/rpm.egg"
EGGS = [ENV_EGG, NEW_EGG, STABLE_EGG, RPM_EGG]

logger = logging.getLogger(__name__)


def log(msg):
    print(msg, file=sys.stderr)


def gpg_validate(path):
    if BYPASS_GPG:
        return True

    gpg_template = '/usr/bin/gpg --verify --keyring %s %s %s'
    cmd = gpg_template % (GPG_KEY, path + '.asc', path)
    proc = subprocess.Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    proc.communicate()
    return proc.returncode == 0


def _main():
    """
    attempt to update with current, fallback to rpm
    attempt to collect and upload with new, then current, then rpm
    if an egg fails a phase never try it again
    """
    if os.getuid() != 0:
        sys.exit('Insights client must be run as root.')

    validated_eggs = list(filter(gpg_validate, [STABLE_EGG, RPM_EGG]))

    if not validated_eggs:
        sys.exit("No GPG-verified eggs can be found")

    sys.path = validated_eggs + sys.path

    # new
    import insights
    from insights.client import InsightsClient
    from insights.client.config import InsightsConfig
    config = InsightsConfig().load_all()
    client = InsightsClient(config=config)
    client._main()

    return
    # old
    # try:
    #     # flake8 complains because these imports aren't at the top
    #     import insights
    #     from insights.client import InsightsClient
    #     from insights.client.phase.v1 import get_phases

    #     # handle client instantation here so that it isn't done multiple times in __init__
    #     client = InsightsClient(True, False)  # read config, but dont setup logging
    #     config = client.get_conf()

    #     # handle log rotation here instead of core
    #     if os.path.isfile(config['logging_file']):
    #         log_handler = logging.handlers.RotatingFileHandler(
    #             config['logging_file'], backupCount=3)
    #         log_handler.doRollover()
    #     # we now have access to the clients logging mechanism instead of using print
    #     client.set_up_logging()
    #     logging.root.debug("Loaded initial egg: %s", os.path.dirname(insights.__file__))

    #     if config["version"]:
    #         from insights_client.constants import InsightsConstants as constants
    #         print("Client: %s" % constants.version)
    #         print("Core: %s" % client.version())
    #         return

    #     for p in get_phases():
    #         run_phase(p, client)
    # except KeyboardInterrupt:
    #     sys.exit('Aborting.')


if __name__ == '__main__':
    _main()
