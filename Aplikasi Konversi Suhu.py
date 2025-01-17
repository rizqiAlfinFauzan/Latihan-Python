# Global variable to store Celcius value
nilai_celcius = 0

def celcius():
    global nilai_celcius
    nilai_celcius = int(input("Masukkan nilai Celcius :"))
    print(f"Nilai Suhu adalah {nilai_celcius}\u00B0C")

def reamur():
    print("Konversi Celcius ke Reamur")
    konversi_reamur =  (4/5) * nilai_celcius
    print(f"Suhu : {konversi_reamur}\u00B0R")

def farenheit():
    print("Konversi Celcius ke Farenheit")
    konversi_farenheit =  (nilai_celcius * 9/5) + 32
    print(f"Suhu : {konversi_farenheit}\u00B0F")
                    
def kelvin():
    print("Konversi Celcius ke Kelvin")
    konversi_kelvin = nilai_celcius + 273
    print(f"Suhu : {konversi_kelvin}\u00B0K")

def masukkan_nilai_celcius():
    print("\n")
    print("-"*7, 'TAMPILAN AWAL',"-"*7)
    print("[a] Input Nilai Celcius")
    print("[b] Exit")

    mulai = input("Pilih Aksi > ")
    print("\n")

    if mulai == 'a':
        celcius()
        show_menu()  # Panggil show_menu setelah memasukkan nilai Celcius
    elif mulai == 'b':
        exit()
    else:
        print("Terjadi Kesalahan")
        masukkan_nilai_celcius()  # Ulangi jika salah input

def show_menu():
    while True:  # Tambahkan loop agar user bisa memilih beberapa konversi
        print("\n")
        print("-"*7, 'MENU',"-"*7)
        print("[1] Reamur")
        print("[2] Farenheit")
        print("[3] Kelvin")
        print("[4] Input Nilai Celcius Baru")
        print("[5] Exit")

        menu = int(input("Pilih Menu > "))
        print("\n")

        if menu == 1:
            reamur()
        elif menu == 2:
            farenheit()
        elif menu == 3:
            kelvin()
        elif menu == 4:
            masukkan_nilai_celcius()
            break  # Keluar dari loop dan mulai ulang dengan nilai baru
        elif menu == 5:
            exit()
        else:
            print("Salah Pilih")

#program utama
masukkan_nilai_celcius()