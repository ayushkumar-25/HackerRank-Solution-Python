def minimumNumber(n,p):
    count=0
    if any(i.isdigit() for i in p)==False:
        count+=1
    if any(i.islower() for i in p)== False:
        count+=1
    if any(i.isupper() for i in p )== False:
        count+=1
    if any(i in "!@#$%^&*()_+" for i in p)==False:
        count+=1
    return max(count,6-n)



n = int(input())
password = input()
result = minimumNumber(n,password)
print(result)