from __future__ import unicode_literals

from django.db import models


class Request(models.Model):
    platform = models.ForeignKey('Platform')
    offering = models.ForeignKey('Offering')
    customer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)


class Platform(models.Model):
    name = models.CharField(max_length=100)
    offerings = models.ManyToManyField(
        'Offering',
        blank=True,
        help_text='List of offerings to show for this platform'
    )

    def __unicode__(self):
        return self.name


class Offering(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class PlatformOffering(models.Model):
    """Configuration for an offering on a platform.

    This model exists to configure an offering for a particular platform only.
    It's important to understand that because we don't want to create a
    relation between Request and this PlatformOffering model, because a
    PlatformOffering may not exist at any time for a particular
    platform/offering combination.
    """
    platform = models.ForeignKey(Platform)
    offering = models.ForeignKey(Offering)
    hide_fields = models.CharField(
        max_length=200,
        help_text='List of fields to hide for this combination.',
        blank=True,
        default='',
    )

    class Meta:
        unique_together = (
            ('platform', 'offering'),
        )

    def __unicode__(self):
        return u'%s / %s' % (self.platform, self.offering)
