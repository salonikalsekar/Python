pos = -1
def search(list, n ):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if n > list[mid]:
                l = mid + 1 ;
            else:
                u = mid - 1;
    return False



list = [3,6,77,8,94]

n = 9

if search(list, n):
    print("found at position", pos+1)
else:
    print("not found")