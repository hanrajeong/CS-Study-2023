str = input()
ans = 0
val = 1

opened = []


def sol(s):
    global ans, val
    for i in range(len(s)):
        if s[i] == '(':
            val *= 2
            opened.append(s[i])

        elif s[i] == '[':
            val *= 3
            opened.append(s[i])

        elif s[i] == ')':
            if not opened or opened[-1] == '[':
                ans = 0
                return
            if s[i-1] == '(':
                ans += val
            val //= 2
            opened.pop()

        elif s[i] == ']':
            if not opened or opened[-1] == '(':
                ans = 0
                return
            if s[i-1] == '[':
                ans += val
            val //= 3
            opened.pop()
    if opened:
        ans = 0


sol(str)
print(ans)
