# def solution(numbers, hand):
#     a = {1: (0, 0), 2: (0, 1), 3: (0, 2),
#          4: (1, 0), 5: (1, 1), 6: (1, 2),
#          7: (2, 0), 8: (2, 1), 9: (2, 2),
#          '*': (3, 0), 0: (3, 1), '#': (3, 2)}
#
#     answer = ''
#     r = '#'
#     l = '*'
#
#     for num in numbers:
#         #왼손 클릭
#         if num == 1 or num == 4 or num == 7:
#             answer += "L"
#             l = num
#
#         #오른손 클릭
#         elif num == 3 or num == 6 or num == 9:
#             answer += "R"
#             r = num
#
#         #중앙 버튼
#         else:
#             #왼손,중앙 숫자 거리
#             left_distance = abs(a[l][0] - a[num][0]) + abs(a[l][1] - a[num][1])
#             #오른손, 중앙 숫자 거리
#             right_distance = abs(a[r][0] - a[num][0]) + abs(a[r][1] - a[num][1])
#
#             #왼손 거리가 더 가까울때
#             if left_distance < right_distance:
#                 answer += "L"
#                 l = num
#
#             #오른손 거리가 더 가까울때
#             elif left_distance > right_distance:
#                 answer += "R"
#                 r = num
#
#             #거리 같을때
#             elif left_distance == right_distance:
#                 if hand == "left":
#                     answer += "L"
#                     l = num
#                 elif hand == "right":
#                     answer += "R"
#                     r = num
#     return answer
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"
# print(solution(numbers, hand))