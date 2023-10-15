#Nama   : Yasmin Alya Aziza
#NIM    : 2309116036

#Menghitung volume bangun ruang

print("----------------------------------------------------")
print("           Menghitung Volume Bangun Ruang           ")
print("----------------------------------------------------")

#Pilihan  bentuk bangun ruang

print("Program Menghitung Volume Bangun Ruang :")
print("[1] Volume Bangun Ruang Bola")
print("[2] Volume Bangun Ruang Tabung")
print("[3] Volume Bangun Ruang Limas Segitiga")
print("----------------------------------------------------")
bangun_ruang = int(input("Pilih salah satu program dari 1 sampai 3 : "))

if bangun_ruang == 1:
    print("----------------------------------------------------")
    print("     Program Menghitung Volume Bangun Ruang Bola    ")
    print("----------------------------------------------------")
    
    r = float(input("Masukkan nilai Jari-jari : "))
    
    if r % 7 == 0 :
        phi = 22/7
    
    elif r % 7 != 0 :
        phi = 3.14
    
    else:
        print("Error. Input kembali angka yang benar")
    
    volume_bola = 4/3 * phi * r ** 3
    print(f"Hasil volume bola adalah {volume_bola}")

elif bangun_ruang == 2:
    print("----------------------------------------------------")
    print("    Program Menghitung Volume Bangun Ruang Tabung   ")
    print("----------------------------------------------------")
    
    print("Pilihan untuk menggunakan jari-jari atau diameter : ")
    print("[1] Menggunakan jari-jari atau radius")
    print("[2] Menggunakan diameter")
    
    radius_atau_diameter = int(input("Pilih salah satu program dari 1 sampai 2 : "))
    
    if radius_atau_diameter == 1 :
        print("-------------------------------------------------")
        print("Program Menghitung Volume Tabung dengan jari-jari")
        print("-------------------------------------------------")
        t = float(input("Masukkan nilai Tinggi : "))
        r = float(input("Masukkan nilai Jari-jari : "))
        if r % 7 == 0 :
            phi = 22/7
            
        elif r % 7 != 0 :
            phi = 3.14
            
        else:
            print("Error. Input kembali angka yang benar")
            
        volume_tabung = phi * r ** 2 * t
        print(f"Hasil volume tabung adalah {volume_tabung}")
            
    elif radius_atau_diameter == 2 :
        print("-------------------------------------------------")
        print("Program Menghitung Volume Tabung dengan diameter ")
        print("-------------------------------------------------")
        t = float(input("Masukkan nilai Tinggi : "))
        d = float(input("Masukkan nilai Diameter : "))
        
        if d % 7 == 0 :
            phi = 22/7
            
        elif d % 7 != 0 :
            phi = 3.14
            
        else:
            print("Error. Input kembali angka yang benar")
            
        volume_tabung = phi * (1/2*d) ** 2 * t
        print(f"Hasil volume tabung adalah {volume_tabung}")
            
    else:
        print("Error. Input kembali angka yang benar")

elif bangun_ruang == 3:
    print("-----------------------------------------------------")
    print("Program Menghitung Volume Bangun Ruang Limas Segitiga")
    print("-----------------------------------------------------")
    
    print("Pilihan untuk mencari volume atau bukan : ")
    print("[1] Mencari volume")
    print("[2] Bukan mencari volume")
    
    volume_atau_bukan = int(input("Pilih salah satu program dari 1 sampai 2 : "))
    
    if volume_atau_bukan == 1 :
        print("----------------------------------------")
        print("Program Menghitung Volume Limas Segitiga")
        print("----------------------------------------")
        luas_alas = float(input("Masukkan nilai Luas Alas : "))
        t = float(input("Masukkan nilai Tinggi Limas Segitiga : "))
        volume_limas_segitiga = 1/3 * luas_alas * t
        print(f"Hasil volume limas segitiga adalah {volume_limas_segitiga}")
        
    elif volume_atau_bukan == 2 :
        print("Error. Input kembali angka yang benar")
        
    else:
        print("Error. Input kembali angka yang benar")

else:
        print("Error. Input kembali angka yang benar")