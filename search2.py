def search(L,N):
    for i in L:
        if(i == N):
            return "Found"
        return "Not Found"

l = [1,8,9,6,4,7]
n = int(input("Enter the number to search: "))

r = search(l,n)
print(r)
