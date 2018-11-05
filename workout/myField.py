from django.utils.translation import ugettext as _
from django.db import models

DAY_OF_THE_WEEK = {
    '1': _(u'Monday'),
    '2': _(u'Tuesday'),
    '3': _(u'Wednesday'),
    '4': _(u'Thursday'),
    '5': _(u'Friday'),
    '6': _(u'Saturday'),
    '7': _(u'Sunday'),
}

NUMBER_OF_THE_WEEK = {
    '1': _(u'First'),
    '2': _(u'Second'),
    '3': _(u'Third'),
    '4': _(u'Fourth'),
}


class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


class NumberOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(NUMBER_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(NumberOfTheWeekField, self).__init__(*args, **kwargs)
