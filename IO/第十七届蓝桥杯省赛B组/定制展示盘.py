"""
输入格式
第一行包含一个正整数 T，表示数据的组数。
接下来的 T 行，每行包含一个正整数 n，代表小蓝拥有的纪念币总数。

输出格式
输出共 T 行，每行包含一个整数，表示在符合所有要求的情况下，展示盘最少需要包含的槽位总数。

输入
2
3
5

输出
4
6

说明/提示
【样例说明】
当 n=3 时，一种最优方案是定制一个 2×2 的展示盘，此时总槽位数为 4；
当 n=5 时，一种最优方案是定制一个 2×3 的展示盘，此时总槽位数为 6。
"""
import math

T = int(input())
for i in range(T):
    n = int(input())

    # n <= 4 时，最小面积就是 2x2=4
    if n <= 4:
        print(4)
        continue

    # 初始化答案为一个大数
    ans = float('inf')
    # 枚举行数 r 从 2 到 sqrt(n)+1
    for r in range(2, int(math.isqrt(n)) + 2):
        # 列数 c 要满足 c >= 2 且 r*c >= n
        c = (n + r - 1) // r  # 向上取整
        if c < 2:
            c = 2
        area = r * c
        if area < ans:  # 用最小面积的组合表示最优解
            ans = area
    print(ans)