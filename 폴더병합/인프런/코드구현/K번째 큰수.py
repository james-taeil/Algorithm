'''
1~100중 3장의 카드를 뽑아서 K번째 값을 출력
'''

'''
코드구현 생각
중복 제거를 하는게 중요
set()을 쓰자 /// set자료 구조는 append가 아니고 add(a[i] + a[j], a[k])

내림 차순 list.sort(reverse=True)

for 문 3개를 돌려 n개중 i 번째, n개중 i + 1 번째, n 개중 j + 1 번째로 
중복 숫자 선택 안되고 앞에꺼 부터 끝숫자까지 돌게 해서 저장
'''

# for i in range(N):
#     for j in range(i+1, N):
#         for m in range(j+1, N):
#             set().add(a[i] + a[j], a[m])

