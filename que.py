
def pat(k):
    if k==0:
        return 'a'
    elif k==1:
        return 'bc'
    else:
        return pat(k-2)+pat(k-1)

x=int(input("Enter the number:- "))
ans=list(pat(x))
y=int(input("Enter index:- "))
print(ans[y])
