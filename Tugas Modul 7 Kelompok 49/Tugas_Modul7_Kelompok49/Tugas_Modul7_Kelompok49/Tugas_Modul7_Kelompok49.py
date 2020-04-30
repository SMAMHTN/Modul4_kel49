a = 1
stack = []
show = []
print("Ganjil/Genap Stack Kelompok 49")
print("1. Add Number")
print("2. Batch Add Number")
print("3. Remove Spesific Number")
print("4. Remove Highest Number")
print("5. Remove Lowest Number")
print("6. Lihat Daftar Data (Lengkap)")
print("7. Lihat Daftar Data (Ganjil)")
print("8. Lihat Daftar Data (Genap)")
print("9. About Creator")
print("0. Show All Feature")
print("99. Reset Number")
while a == 1:
    choice = int(input("Masukkan Pilihan : "))

    if choice == 1: #add item
        print("Add Number")
        b = int(input("Add Number : "))
        stack.append(b)
        print ("-"*40) 

    elif choice == 2: #Batch add item
        print("Batch Add Number")
        b = int(input("Add initial Number : "))
        c = int(input("Add Last Number : "))
        d = int(input("Add Selisih antar-Angka : "))
        c=c+1
        if d==0:
            print("Selisih tidak bisa 0")
            print ("-"*40)
        else:
            for x in range(b,c,d):
                stack.append(x)
            print ("-"*40)

    elif choice == 3: #Remove Spesific Number
        print("Remove Spesific Number")
        b = int(input("Remove Number : "))
        if b not in stack :
            print(f"Sorry,{b} not found ")
        else :
            stack.remove(b)
        print ("-"*40)

    elif choice == 4: #Remove Highest Number
        print("Remove Highest Number")
        stack.sort()
        stack.pop()
        print ("-"*40)

    elif choice == 5: #Remove Lowest Number
        print("Remove Lowest Number")
        stack.sort()
        stack.popleft()
        print ("-"*40)

    elif choice == 6: #Show Stack
        print("Lihat Daftar Data (Lengkap)")
        stack.sort()
        print(stack)
        print ("-"*40)

    elif choice == 7: #Show Stack (Ganjil)
        print("Lihat Daftar Data (Ganjil)")
        stack.sort()
        for x in stack :
            if x%2==1 :
                show.append(x)
        print(show)
        del show[:]
        print ("-"*40)

    elif choice == 8: #Show Stack (Genap)
        print("Lihat Daftar Data (Genap)")
        stack.sort()
        for x in stack :
            if x%2==0 :
                show.append(x)
        print(show)
        del show[:]
        print ("-"*40)

    elif choice == 9:
        print("About Creator")
        print("Program ini dibuat oleh kelompok 49 Shift 2")
        print("Aldi Mulyawan 21120119120026")
        print("Mochamad Pratama Wibawa 21120119130062")
        print ("-"*40)

    elif choice == 0:
        print("Show All Feature")
        print("1. Add Number")
        print("2. Batch Add Number")
        print("3. Remove Spesific Number")
        print("4. Remove Highest Number")
        print("5. Remove Lowest Number")
        print("6. Lihat Daftar Data (Lengkap)")
        print("7. Lihat Daftar Data (Ganjil)")
        print("8. Lihat Daftar Data (Genap)")
        print("9. About Creator")
        print("0. Show All Feature")
        print("99. Reset Number")

    elif choice == 99:
        del stack[:]
        print("All Numbers has been deleted")

    else :
        print("Feature not found")

