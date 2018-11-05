import django
import os
import pandas as pd
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Prity.settings")
django.setup()
from workout_info.models import Part, WorkoutInfo

'''
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
'''
streching = Part.objects.get(part='0')
triceps = Part.objects.get(part='1')
biceps = Part.objects.get(part='2')
shoulder = Part.objects.get(part='3')
chest = Part.objects.get(part='4')
back = Part.objects.get(part='5')
core = Part.objects.get(part='6')
thigh = Part.objects.get(part='7')
calf = Part.objects.get(part='8')
hip = Part.objects.get(part='9')
cardio = Part.objects.get(part='10')


df = pd.read_excel('workout_info.xlsx')
list = df.index.tolist()
for index in list:
    w = WorkoutInfo()
    part = df['part'][index]
    if part == '유산소':
        w.part = cardio
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '가슴':
        w.part = chest
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '삼두근':
        w.part = triceps
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '이두근':
        w.part = biceps
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '어깨':
        w.part = shoulder
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '등':
        w.part = back
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '허벅지':
        w.part = thigh
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '종아리':
        w.part = calf
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    elif part == '복근':
        w.part = core
        w.eng_name = df['eng_name'][index]
        w.kor_name = df['kor_name'][index]
        w.save()
    print(w, index)

