def divisible5(n):
    if (n%5==0):
        return True
    return False

a=[112,34556,234562,1234565,98732,51120,876,12355]

f=list(filter(divisible5,a))
print(f)
