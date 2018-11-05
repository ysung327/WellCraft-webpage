from django.test import TestCase

# Create your tests here.
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
    else:
        p = None
    return p

p = name_to_index('유산소')
print(p)
