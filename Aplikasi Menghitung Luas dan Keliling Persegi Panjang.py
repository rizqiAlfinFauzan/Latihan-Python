import os
def header():
    # Header
    os.system('cls') #sistem loperasi windows
    print(f'{'PROGRAM MENGIHTUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print(f'{'-'*40:^40}')

def input_user():
    # Mengambil Input User
    lebar = int(input('Masukkan Nilai Lebar: '))
    panjang = int(input('Masukkan Nilai Panjang: '))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    # Fungsi Luas
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    # Fungsi Keliling
    return 2*(lebar+panjang)

def display(message,value):
    # Fungsi Display
    print(f'{message} = {value}')

def display_opsi0():
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    display('Luas', LUAS)

def display_opsi1():
    LEBAR,PANJANG = input_user()
    KELILING = hitung_keliling(LEBAR,PANJANG)
    display('Keliling', KELILING)

def display_opsi2():
    LEBAR,PANJANG = input_user()
    KELILING = hitung_keliling(LEBAR,PANJANG)
    LUAS = hitung_luas(LEBAR,PANJANG)
    display('Keliling', KELILING)
    display('Luas', LUAS)


    # Program Utamanya
while True:
    header()
    opsi = input('Pilih Opsi Perhitungan (0 = Luas, 1 = Keliling, 2 = Keduanya): ')
    if opsi == '0':
        display_opsi0()
    elif opsi == '1':
        display_opsi1()
    elif opsi == '2':
        display_opsi2()
    else:
        print('Guoblok Maneh?')

    isContinue = input('Lanjutkan? (y/n)')
    if isContinue == 'n':
        break

print('Program Complete')