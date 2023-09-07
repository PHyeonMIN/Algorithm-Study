# 예제 3-1. 거스름돈
# 가장 큰 화폐 단위부터 돈을 거슬러주기

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 시간 복잡도 O(K)
# : 동전의 총 종류에만 영향을 받는다.
