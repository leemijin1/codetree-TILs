n=input()
arr=n.split()
h=int(arr[0])
w=int(arr[1])
b=w/(h/100)**2

if b>=25:
    print(f'{int(b)}')
    print("Obesity")
else:
    print(f'{int(b)}')