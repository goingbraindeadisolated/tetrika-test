def intersection(interval1:list, interval2:list)->list:
    interval1_start, interval1_end = interval1
    interval2_start, interval2_end = interval2
    if interval1_start > interval2_end or interval1_end < interval2_start:
    # no intersection ->
        return None
    else
        pass

def appearance(intervals):
    pupil_lesson_intersections = []
    pupil_offset = 0
    lesson_offset = 0
    while True:
        interval = intersection(intervals['data']['lesson'][lesson_offset:lesson_offset+2], intervals['data']['pupil'][pupil_offset:pupil_offset+2])
        if interval is not None:
            pupil_lesson_intersections.append(interval) 
            
tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if name == 'main':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
