str='LIRIL'
def pal(str):
    left=0
    right=len(str)-1
    print(left,right)
    while right>=left:
        if not str[left]==str[right]:
            return False

        left+=1
        right-=1
    return True

check=pal(str)
if check==False:
    print("not palindrome")
else:
    print("palindrome")