from horizon import tabs
from .tables import MonitorTable
import get_data

import utils

class DataTab(tabs.TableTab):
    name = _("Data")
    slug = 'data'
    table_classes = (MonitorTable,)
    template_name = 'horizon/common/_detail_table.html'
    preload = False

    def get_instances_data(self):
        return utils.get_instances_data(self.request)
	#return get_data.get_instances_data(self.request)
'''
class VizTab(tabs.Tab):
    name = _("Visualization")
    slug = "viz"
    template_name = "visualizations/flocking/_flocking.html"

    def get_context_data(self, request):
    	return None
'''

class AlarmTab(tabs.TableTab):
    name = ("Alarms")
    slug = 'alarms'
    table_classes = (MonitorTable,)
    template_name = 'horizon/common/_detail_table.html'
    preload = False

    def get_instances_data(self):
        return utils.get_instances_data(self.request)

class MonitorTabs(tabs.TabGroup):
    slug = 'netmon'
    #tabs = (DataTab, VizTab, AlarmTab)
    tabs = (DataTab, AlarmTab)
