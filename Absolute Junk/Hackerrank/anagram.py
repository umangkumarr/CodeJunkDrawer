

def intersection(lst1,lst2):
    lst3=[]
    for value in lst1:
        if value in lst2:
            lst3.append(value)
            lst2.remove(value)
    return len(lst3)
def anagram(s):
    l=len(s)
    if l%2!=0:
        return -1
    else:
        lst1=s[:l//2]
        lst2=s[l//2:]
        return l//2-intersection(list(lst1),list(lst2))
print(anagram('fdhlvosfpafhalll'))

