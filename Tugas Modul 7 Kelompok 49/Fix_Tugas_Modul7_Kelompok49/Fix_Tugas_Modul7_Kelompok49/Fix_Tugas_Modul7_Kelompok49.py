stack=[]
stack_ganjil=[]
stack_genap=[]
z=1
for x in range(1,51,1):
    stack.append(x)
for y in stack:
        if y%2==0:
            stack_genap.append(y)
        elif y%2==1:
            stack_ganjil.append(y)

print("Stack Ganjil Genap Kelompok 49")
while z==1:
    print("1.Stack Ganjil")
    print("2.Stack Genap")
    a=int(input("Masukkan Pilihan Anda : "))
    if a==1:
        print("Stack Ganjil : ")
        print(stack_ganjil)
    elif a==2:
        print("Stack Genap : ")
        print(stack_genap)
    else :
        print("Wrong Input")
    print("-"*40)
    stack_genap.remove
    stack_ganjil.remove
