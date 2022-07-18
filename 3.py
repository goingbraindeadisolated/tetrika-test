def intersection(interval1: list, interval2: list) -> list:
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > end2 or end1 < start2:
        # no intersection
        return None
    else:
        if start1 > start2 and end1 > end2:
            '''
                [     ]
            [     ]
            '''
            print('1')
            return [start1, end2]
        elif start1 < start2 and end1 > end2:
            '''
            [     ]
              []
            '''
            print('4')
            return [start2, end2]
        elif start1 < start2 and end1 < end2:
            '''
            [     ]
                [     ]
            '''
            print('2')
            return [start2, end1]
        elif start1 > start2 and end1 < end2:
            '''
              []
            [     ]
            '''
            print('3')
            return [start1, end1]
        else:
            raise Exception(f'intersection error: {interval1}, {interval2}')


def appearance(intervals):
    pupil_lesson_intersections = []
    pupil_offset = 0
    lesson_offset = 0 
    while lesson_offset+1 < len(intervals['lesson']) and pupil_offset+1 < len(intervals['pupil']):
        interval1 = intervals['lesson'][lesson_offset:lesson_offset+2]
        interval2 = intervals['pupil'][pupil_offset:pupil_offset+2]
        result_interval = intersection(interval1, interval2)
        print(interval1, interval2, result_interval, sep=' : ')
        if result_interval is not None:
            pupil_lesson_intersections += result_interval
        if interval1[1] > interval2[1]:
            '''
            .......]
            ...]
            '''
            pupil_offset += 2
        else:
            '''
            ...]
            .......]
            '''
            lesson_offset += 2
    print(pupil_lesson_intersections)
    
    pupil_tutor_intersections = []
    pupil_lesson_offset = 0
    tutor_offset = 0 
    while pupil_lesson_offset+1 < len(pupil_lesson_intersections) and tutor_offset+1 < len(intervals['tutor']):
        interval1 = pupil_lesson_intersections[pupil_lesson_offset:pupil_lesson_offset+2]
        interval2 = intervals['tutor'][tutor_offset:tutor_offset+2]
        result_interval = intersection(interval1, interval2)
        print(interval1, interval2, result_interval, sep=' : ')
        if result_interval is not None:
            pupil_tutor_intersections.append(result_interval)
        if interval1[1] > interval2[1]:
            '''
            .......]
            ...]
            '''            
            tutor_offset += 2
        else:
            '''
            ...]
            .......]
            '''
            pupil_lesson_offset += 2
    print(pupil_tutor_intersections)
    return sum([i[1] - i[0] for i in pupil_tutor_intersections])
    
tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

