from django.utils.translation import ugettext as _
from django.db import models

PART_OF_THE_WORKOUT = {
    '0': _(u'스트레칭'),
    '1': _(u'삼두근'),
    '2': _(u'이두근'),
    '3': _(u'어깨'),
    '4': _(u'가슴'),
    '5': _(u'등'),
    '6': _(u'복근'),
    '7': _(u'허벅지'),
    '8': _(u'종아리'),
    '9': _(u'엉덩이'),
    '10': _(u'유산소'),
}

ENG_NAME_OF_THE_WORKOUT = {
    '0': _(u'Streching'),
    '1': _(u'Triceps'),
    '2': _(u'Biceps'),
    '3': _(u'Shoulders'),
    '4': _(u'Chest'),
    '5': _(u'Back'),
    '6': _(u'Core'),
    '7': _(u'Thigh'),
    '8': _(u'Calf'),
    '9': _(u'Hip'),
    '10': _(u'Cardio'),
}


class PartOfTheWorkout(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(PART_OF_THE_WORKOUT.items()))
        kwargs['max_length'] = 1
        super(PartOfTheWorkout, self).__init__(*args, **kwargs)

    def get_part_name(key):
        dict = PART_OF_THE_WORKOUT
        return dict.get(key)


class EngNameOfTheWorkout(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(ENG_NAME_OF_THE_WORKOUT.items()))
        kwargs['max_length'] = 1
        super(EngNameOfTheWorkout, self).__init__(*args, **kwargs)

    def get_part_name(key):
        dict = ENG_NAME_OF_THE_WORKOUT
        return dict.get(key)
