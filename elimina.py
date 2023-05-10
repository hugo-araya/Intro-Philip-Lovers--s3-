a = "abcdefcgggcddcddc"
b = ""
largo = len(a)
i = 0
while i < largo:
    if a[i] != "c":
        b = b + a[i]
    i = i + 1
print(b)

