"""AUFREISSEN"""

def generate(s):
    n = len(s)
    results = set()

    def dfs(i, cur):
        if i == n:
            results.add(cur)
            return
        if s[i] == 'S':
            # 1. 单独处理这个 S -> s
            dfs(i + 1, cur + 's')
            # 2. 如果后面还有 S，可以当作 SS 组处理
            if i + 1 < n and s[i + 1] == 'S':
                dfs(i + 2, cur + 'B')   # ß 用 B 表示
                dfs(i + 2, cur + 'ss')
        else:
            dfs(i + 1, cur + s[i].lower())

    dfs(0, "")
    return sorted(results)   # 返回列表，不是字符串

s = input()
for word in generate(s):
    print(word)