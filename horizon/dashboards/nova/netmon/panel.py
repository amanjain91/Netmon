from django.utils.translation import ugettext_lazy as _

import horizon

##from openstack_dashboard.dashboards.project import dashboard
from horizon.dashboards.nova import dashboard

class Netmon(horizon.Panel):
    name = _("Netmon")
    slug = "netmon"


dashboard.Nova.register(Netmon)
