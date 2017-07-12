"""
Constants
"""

class InsightsConstants(object):
    app_name = 'insights-client'
    version = '3.0.0-0'
    default_ansible_inventory = 'localhost'
    ansible_command = 'ansible %s -m insights'
    ansible_library_path = "/etc/insights-client/insights/"
    ansible_action_plugins_path = '/etc/insights-client/insights/action_plugins/'
    