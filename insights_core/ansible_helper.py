"""
Ansible
"""
import sys
import os
from constants import InsightsConstants as constants
from utilities import InsightsUtilities

class InsightsAnsible(object):
    

    def __init__(self, core, inventory=None, egg_path=None):
        self.ansible = None
        self.ansible_loaded = False
        self.core = core
        self.inventory = inventory
        self.egg_path = egg_path
        self.utilities = InsightsUtilities()
        self.load_ansible()

    def load_ansible(self):
        try:
            import ansible
            self.ansible = ansible
            self.ansible_loaded = True
            return True
        except Exception:
            return False

    def get_egg_path(self):
        import pkgutil
        package = pkgutil.get_loader('insights_core')
        location_to_the_egg = package.archive
        return location_to_the_egg

    def run(self):
        try:
            inventory = self.inventory if self.inventory is not None else constants.default_ansible_inventory
            egg_path = self.egg_path if self.egg_path is not None else self.get_egg_path()
            ansible_command = constants.ansible_command % (inventory)
            env = os.environ.copy()
            env['ANSIBLE_LIBRARY'] = constants.ansible_library_path
            env['ANSIBLE_ACTION_PLUGINS'] = constants.ansible_action_plugins_path
            ansible_execution = self.utilities.run_command_get_output(ansible_command, env)
        except Exception as an_exception:
            sys.exit("Could not run the Ansible action plugin and module. Exiting.")
