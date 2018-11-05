from django.shortcuts import render, redirect
from django.http import JsonResponse
from workout.models import MonthWeekNum
from workout_info.models import WorkoutInfo, Part
import datetime

# Create your views here.
def my_workout_view(request):
    if request.user.is_active:
        current_user = request.user

        # 날짜 가져오기
        now = datetime.datetime.now()
        dic = MonthWeekNum(now)  # 만약에 이동버튼으로 request 들어오면 now값을 +7 -7해서 내보내기. ajax로 해결.
        monday = dic['monday']
        day = ['월', '화', '수', '목', '금', '토', '일']

        # part 가져오기
        part = ['스트레칭', '삼두근', '이두근', '어깨', '가슴', '등', '복근', '허벅지', '종아리', '엉덩이', '유산소']

        context = {
            'user': current_user,
            'monday': dic['monday'],
            'month': dic['mon'],
            'week': dic['weekNum'],
            'days': day,
            'part': part
        }
        return render(request, 'workout/my_workout.html', context)
    else:
        return redirect('accounts:my-account')


def name_to_index(part):
    p = 0
    if part == '스트레칭':
        p = 0
    elif part == '삼두근':
        p = 1
    elif part == '이두근':
        p = 2
    elif part == '어깨':
        p = 3
    elif part == '가슴':
        p = 4
    elif part == '등':
        p = 5
    elif part == '복근':
        p = 6
    elif part == '허벅지':
        p = 7
    elif part == '종아리':
        p = 8
    elif part == '엉덩이':
        p = 9
    elif part == '유산소':
        p = 10
    return p


def load_workout_list(request):
    part = request.GET.get('part')
    p = name_to_index(part)
    workout = WorkoutInfo.objects.filter(part__part=p)
    context = {
        'workout': workout
    }

    return render(request, 'workout/workout_list.html', context)
