# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_apphook_setup.base import AutoCMSAppMixin

from .cms_appconfig import App6Config


class App6(AutoCMSAppMixin, CMSConfigApp):
    name = _('App6')
    urls = ['sample_app_6.urls']
    app_name = 'app6'
    app_config = App6Config
    auto_setup = {
        'enabled': True,
        'home title': 'home title',
        'page title': 'page 6 title',
        'namespace': 'namespace',
        'config_fields': {'random_option': True},
        'config_translated_fields': {'app_title': 'app title', 'object_name': 'name'},
        'sites': [2]
    }

apphook_pool.register(App6)
App6.setup()
