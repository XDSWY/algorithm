"""
题目描述
2056 年，探险队在月球背面的环形山深处发现了一座信号发射塔，其核心控制台正在不断闪烁着一串长度为 N 的粒子序列。
序列中的每个位置被严格定义为 L 型粒子、Q 型粒子，或者因岁月侵蚀而模糊不清的未知状态 ?。
这些粒子将被依次射入反应场，而反应场的稳定性取决于序列的“LQ 聚合”数量，
该数量被定义为所有满足 1≤i<j≤N 且第 i 个节点为 L、第 j 个节点为 Q 的二元组数量。
为了重启这座沉睡的巨塔，探险队需要将序列中所有的 ? 修复为确定的 L 或 Q。
现在，请你计算出在所有可能的修复方案中，所能得到的“LQ 聚合”数量的最大值是多少。

输入格式
第一行输入一个整数 N，表示粒子序列的长度。
第二行输入一个长度为 N 的字符串，仅包含字符 L、Q 和 ?，表示当前探测到的粒子序列状态。

输出格式
输出一个整数，表示在将所有 ? 替换为 L 或 Q 后，能获得的最大“LQ 聚合”数量。

输入
5
??L??

输出
6
"""

def solve2():
    N = int(input())
    s = input().strip()
    fixL = s.count('L')
    fixQ = s.count('Q')
    unk = N - fixL - fixQ
    target = (N - fixQ + fixL) // 2
    target = max(0, min(unk, target))
    # 然后检查 target 和 target+1
    best = 0
    for x in [target, target+1, target-1, target+2]:
        if 0 <= x <= unk:
            L = fixL + x
            Q = fixQ + unk - x
            best = max(best, L * Q)
    print(best)