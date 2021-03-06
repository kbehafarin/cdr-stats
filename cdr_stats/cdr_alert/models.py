#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from country_dialcode.models import Country
from cdr_alert.constants import PERIOD, STATUS, ALARM_TYPE, \
    ALERT_CONDITION, ALERT_CONDITION_ADD_ON, ALARM_REPROT_STATUS


class AlertRemovePrefix(models.Model):
    """This defines the Alert Remove Prefix
    Define the list of prefixes that need to be removed from the dialed digits, 
    assuming the phone numbers are in the format 5559004432, with the signifcant digits
    9004432, the prefix 555 needs to be removed to analyse the phone numbers.

    **Attributes**:

        * ``label`` - Label for the custom prefix
        * ``prefix`` - Prefix value

    **Name of DB table**: alarm
    """
    label = models.CharField(max_length=100, verbose_name=_('Label'))
    prefix = models.CharField(max_length=100, unique=True,
                              verbose_name=_('Prefix'))
    created_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name=_('Date'))
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % (self.label)

    class Meta:
        verbose_name = _("Alert Remove Prefix")
        verbose_name_plural = _("Alert Remove Prefixes")
        db_table = "alert_remove_prefix"


class Alarm(models.Model):
    """This defines the Alarm

    **Attributes**:

        * ``user`` -
        * ``name`` - Alarm name
        * ``period`` - Day | Week | Month
        * ``type`` - ALOC (average length of call) ; ASR (answer seize ratio)
        * ``alert_condition`` -
        * ``alert_value`` - Input the value for the alert
        * ``alert_condition_add_on`` -
        * ``status`` - Inactive | Active
        * ``email_to_send_alarm`` - email_to

    **Name of DB table**: alert
    """
    user = models.ForeignKey('auth.User', related_name='Alarm_owner')
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    period = models.PositiveIntegerField(choices=list(PERIOD), default=1,
                                verbose_name=_('Period'),
                                help_text=_('Interval to apply alarm'))
    type = models.PositiveIntegerField(choices=list(ALARM_TYPE), default=1,
                                verbose_name=_('Type'),
                                help_text=_('ALOC (average length of call) ; ASR (answer seize ratio) ; CIC (Consecutive Incomplete Calls) '))
    alert_condition = models.PositiveIntegerField(choices=list(ALERT_CONDITION),
                                                  default=1,
                                                  verbose_name=_('Condition'))
    alert_value = models.DecimalField(verbose_name=_('Value'), max_digits=5,
                                decimal_places=2, blank=True, null=True,
                                help_text=_('Input the value for the alert'))
    alert_condition_add_on = models.PositiveIntegerField(choices=list(ALERT_CONDITION_ADD_ON),
                                                         default=1)
    status = models.PositiveIntegerField(choices=list(STATUS), default=1,
                                         verbose_name=_('Status'))

    email_to_send_alarm = models.EmailField(max_length=100,
                                    verbose_name=_('Email to send alarm'))
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name=_('Date'))
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        permissions = (
            ("view_alarm", _('Can see alarms')),
        )
        verbose_name = _("Alarm")
        verbose_name_plural = _("Alarms")
        db_table = "alert"


class AlarmReport(models.Model):
    """This defines the Alarm report

    **Attributes**:

        * ``alarm`` - Alarm name
        * ``calculatedvalue`` - Input the value for the alert
        * ``daterun`` -

    **Name of DB table**: alert_report
    """
    alarm = models.ForeignKey(Alarm, verbose_name=_('Alarm'),
                              help_text=_("Select Alarm"))
    calculatedvalue = models.DecimalField(verbose_name=_('Calculated value'),
                                          max_digits=10, decimal_places=3,
                                          blank=True, null=True)
    status = models.PositiveIntegerField(choices=list(ALARM_REPROT_STATUS),
                        default=1, verbose_name=_('Status'))

    daterun = models.DateTimeField(auto_now=True, verbose_name=_('Date'))

    def __unicode__(self):
        return '%s' % (self.alarm)

    class Meta:
        permissions = (
            ("view_alarm_report", _('Can see alarm report')),
        )
        verbose_name = _("Alarm Report")
        verbose_name_plural = _("Alarms Report")
        db_table = "alert_report"


class Blacklist(models.Model):
    """This defines the Blacklist

    **Attributes**:

        * ``user`` -
        * ``phonenumber_prefix`` -
        * ``country`` -

    **Name of DB table**: alert_blacklist
    """
    user = models.ForeignKey('auth.User', related_name='Blacklist_owner')
    phonenumber_prefix = models.PositiveIntegerField(blank=False, null=False)
    country = models.ForeignKey(Country, null=True, blank=True,
                                verbose_name=_("Country"),
                                help_text=_("Select Country"))

    def __unicode__(self):
        return '[%s] %s' % (self.id, self.phonenumber_prefix)

    class Meta:
        permissions = (
            ("view_blacklist", _('Can see blacklist country/prefix')),
        )
        verbose_name = _("Blacklist")
        verbose_name_plural = _("Blacklist")
        db_table = "alert_blacklist"


class Whitelist(models.Model):
    """This defines the Blacklist

    **Attributes**:

        * ``user`` -
        * ``phonenumber_prefix`` -
        * ``country`` -

    **Name of DB table**: alert_whitelist
    """
    user = models.ForeignKey('auth.User', related_name='whitelist_owner')
    phonenumber_prefix = models.PositiveIntegerField(blank=False, null=False)
    country = models.ForeignKey(Country, null=True, blank=True,
                                verbose_name=_("Country"),
                                help_text=_("Select Country"))

    def __unicode__(self):
        return '[%s] %s' % (self.id, self.phonenumber_prefix)

    class Meta:
        permissions = (
            ("view_whitelist", _('Can see whitelist country/prefix')),
        )
        verbose_name = _("Whitelist")
        verbose_name_plural = _("Whitelist")
        db_table = "alert_whitelist"
