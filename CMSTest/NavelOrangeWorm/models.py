from django.db import models
from cms.models import CMSPlugin

# Create your models here.

class Event(CMSPlugin):
    name = models.CharField('Event Name', max_length=100)
    desc = models.CharField('Description', max_length=200)

    def get_relations(self):
        eventAssocItems = []
        AssocItems = self.associated_item.all()
        for item in AssocItems:
            eventAssocItems.append('<p><a href="%s">%s</a></p>' % (item.link, item.linkdesc))

        return eventAssocItems

    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.associated_item.all().delete()

        for associated_item in oldinstance.associated_item.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        managed = True

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class eventLink(models.Model):
    link = models.URLField('URL', max_length=100)
    linkdesc = models.CharField('Description', max_length=200)
    plugin = models.ForeignKey(
        Event,
        related_name="associated_item",
        on_delete=models.CASCADE
    )


    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        managed = True

    # Returns the string representation of the model.
    def __str__(self):
        return self.link

class Resource(CMSPlugin):
    name = models.CharField('Resource Name', max_length=100)
    desc = models.CharField('Description', max_length=200)

    def get_relations(self):
        resAssocItems = []
        AssocItems = self.associated_item.all()
        for item in AssocItems:
            resAssocItems.append('<p><a href="%s">%s</a></p>' % (item.link, item.linkdesc))

        return resAssocItems

    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.associated_item.all().delete()

        for associated_item in oldinstance.associated_item.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'
        managed = True

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class resLink(models.Model):
    link = models.URLField('URL', max_length=100)
    linkdesc = models.CharField('Description', max_length=200)
    plugin = models.ForeignKey(
        Resource,
        related_name="associated_item",
        on_delete=models.CASCADE
    )


    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        managed = True

    # Returns the string representation of the model.
    def __str__(self):
        return self.link


class Resource_view(models.Model):
    resid = models.IntegerField()
    name = models.CharField('Resource Name', max_length=100)
    desc = models.CharField('Description', max_length=200)


    class Meta:
        verbose_name = 'Resource_view'
        verbose_name_plural = 'Resources_view'
        managed = False
        db_table = 'res_view'

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class resLink_view(models.Model):
    resid = models.IntegerField()
    link = models.URLField('URL', max_length=100)
    linkdesc = models.CharField('Description', max_length=200)



    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        managed = False
        db_table = "reslink_view"

    # Returns the string representation of the model.
    def __str__(self):
        return self.link

class Event_view(models.Model):
    evid = models.IntegerField()
    name = models.CharField('Event Name', max_length=100)
    desc = models.CharField('Description', max_length=200)


    class Meta:
        verbose_name = 'Event_view'
        verbose_name_plural = 'Events_view'
        managed = False
        db_table = 'event_view'

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class eventLink_view(models.Model):
    evid = models.IntegerField()
    link = models.URLField('URL', max_length=100)
    linkdesc = models.CharField('Description', max_length=200)



    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        managed = False
        db_table = "eventlink_view"

    # Returns the string representation of the model.
    def __str__(self):
        return self.link