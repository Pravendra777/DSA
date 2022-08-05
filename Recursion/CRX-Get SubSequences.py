def subsequences(s):
    if s == "":
        return [""]
    else:
        return [s[0] + sub for sub in subsequences(s[1:])] + subsequences(s[1:])
a=subsequences("abc")
b=a[:]
print(a[::-1])
print(b)