
def show_reverse(s):
    for i in s[-1::-1]:
        print(i,end=" ")
def sum_all(s):
    sum = 0
    for i in range(len(s)):
        sum += s[i]
    return sum

print(sum_all([1,2,3,4,5]))
show_reverse("ABCDEF")


