from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from NavelOrangeWorm.models import Event, eventLink, Resource, resLink
from django.utils.translation import gettext as _


class EventInline(admin.StackedInline):
    model = eventLink
    extra = 0


class ResInline(admin.StackedInline):
    model = resLink
    extra = 0


@plugin_pool.register_plugin  # register the plugin
class EventClass(CMSPluginBase):
    model = Event # model where plugin data are saved
    module = _("Events")
    name = _("Event Plugin")  # name of the plugin in the interface
    render_template = "event_plugin.html"
    inlines = (EventInline,)
    allow_children = True

    def render(self, context, model, placeholder):
        context.update({"instance": model})
        return context


@plugin_pool.register_plugin
class ResClass(CMSPluginBase):
    model = Resource # model where plugin data are saved
    module = _("Resources")
    name = _("Resource Plugin")  # name of the plugin in the interface
    render_template = "res_plugin.html"
    inlines = (ResInline,)
    allow_children = True

    def render(self, context, model, placeholder):
        context.update({"instance": model})
        return context