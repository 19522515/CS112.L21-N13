
n = int(input())
x = list(map(int, input().split()))

def H_Index(n, x):
    x.sort(reverse=True)
    h_index = 0
    for i in range(n):
        if x[i] >= i + 1:
            h_index += 1
        else:
            break
    return h_index

print(H_Index(n, x))
https://i0.wp.com/s1.uphinh.org/2021/04/02/huanhoahong-1_ugww.jpg
    https://uphinh.org/image/ybcUYu
![Image of Yaktocat](https://i0.wp.com/s1.uphinh.org/2021/04/02/huanhoahong-1_ugww.jpg)
