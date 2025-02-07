import os

# Konstanta
MAKSMHS = 3

# Subrutin menentukan indeks nilai
def IndeksNilai(Nilai):
    if 80 <= Nilai <= 100:
        return 'A'
    elif 70 <= Nilai < 80:
        return 'B'
    elif 60 <= Nilai < 70:
        return 'C'
    elif 50 <= Nilai < 60:
        return 'D'
    else:
        return 'E'

# Subrutin memasukkan elemen array NIM, nama mahasiswa dan nilai akhir
def IsiDataMhs(NIM, Nama, NA, Indeks):
    i = 0
    while i < MAKSMHS:
        print(f'\nData Nilai Mahasiswa Ke-{i + 1}')
        print('--------------------------')
        NIM[i] = str(input('Nomor Induk Mahasiswa  : ')).upper()
        if NIM[i] == 'STOP':
            break
        Nama[i] = str(input('Nama Mahasiswa        : ')).upper()
        NA[i] = float(input('Nilai Akhir           : '))
        Indeks[i] = IndeksNilai(NA[i])
        i += 1
    return i

# Subrutin menampilkan data nilai mahasiswa
def TampilDataMhs(NIM, Nama, NA, Indeks, Kelas, MatKul, N):
    print('DAFTAR NILAI MAHASISWA')
    print(f'Kelas       : {Kelas}')
    print(f'Mata Kuliah : {MatKul}')
    print('----------------------------------------------------------')
    print('| No |    NIM    |    Nama Mahasiswa    | Nilai | Indeks |')
    print('----------------------------------------------------------')
    for i in range(N):
        print(f'| {i + 1:>2} | {NIM[i]:9} | {Nama[i]:20} | {NA[i]:>5.1f} |   {Indeks[i]:1}    |')
    print('----------------------------------------------------------')

# Subrutin mengurutkan NIM secara ascending (Bubble Sort)
def UrutNIMAsc(NIM, Nama, NA, Indeks, N):
    for i in range(N - 1):
        for j in range(N - 1, i, -1):
            if NIM[j] < NIM[j - 1]:
                # Tukar NIM
                NIM[j], NIM[j - 1] = NIM[j - 1], NIM[j]
                # Tukar Nama
                Nama[j], Nama[j - 1] = Nama[j - 1], Nama[j]
                # Tukar Nilai Akhir
                NA[j], NA[j - 1] = NA[j - 1], NA[j]
                # Tukar Indeks
                Indeks[j], Indeks[j - 1] = Indeks[j - 1], Indeks[j]

# Subrutin mencari NIM menggunakan Binary Search
def CariNIM(NIM, Nama, NA, Indeks, N):
    NIMCari = str(input('NIM yang dicari : ')).upper()
    Ia, Ib = 0, N - 1
    Ketemu = False
    k = -1
    while not Ketemu and Ia <= Ib:
        k = (Ia + Ib) // 2
        if NIM[k] == NIMCari:
            Ketemu = True
        elif NIM[k] < NIMCari:
            Ia = k + 1
        else:
            Ib = k - 1
    os.system('cls')
    print('<< HASIL PENCARIAN >>')
    if Ketemu:
        print(f'NIM yang Dicari   : {NIMCari}')
        print(f'Nama Mahasiswa    : {Nama[k]}')
        print(f'Nilai Akhir       : {NA[k]}')
        print(f'Indeks Nilai      : {Indeks[k]}')
    else:
        print(f'NIM {NIMCari} Tidak Ditemukan!')

# Subrutin mencari Nilai Akhir menggunakan Sequential Search
def CariNilai(NIM, Nama, NA, Indeks, N):
    NACariMin = float(input('Nilai yang dicari (Minimal)  : '))
    NACariMax = float(input('Nilai yang dicari (Maksimal) : '))
    os.system('cls')
    print('<< HASIL PENCARIAN >>')
    print('DAFTAR NILAI MAHASISWA')
    print(f'Nilai Akhir : {NACariMin} sampai {NACariMax}')
    print('----------------------------------------------------------')
    print('| No |    NIM    |    Nama Mahasiswa    | Nilai | Indeks |')
    print('----------------------------------------------------------')
    No = 0
    for i in range(N):
        if NACariMin <= NA[i] <= NACariMax:
            No += 1
            print(f'| {No:>2} | {NIM[i]:9} | {Nama[i]:20} | {NA[i]:>5.1f} |   {Indeks[i]:1}    |')
    if No == 0:
        print(f'Nilai Akhir {NACariMin} - {NACariMax} Tidak Ditemukan!')
    print('----------------------------------------------------------')

# Subrutin mencari Nilai Akhir menggunakan Sequential Search untuk Indeks
def CariIndeks(NIM, Nama, NA, Indeks, N):
    IndeksCari = str(input('Indeks yang dicari : ')).upper()
    os.system('cls')
    print('<< HASIL PENCARIAN >>')
    print('DAFTAR NILAI MAHASISWA')
    print(f'Indeks Nilai : {IndeksCari}')
    print('-------------------------------------------------')
    print('| No |    NIM    |    Nama Mahasiswa    | Nilai |')
    print('-------------------------------------------------')
    No = 0
    for i in range(N):
        if Indeks[i] == IndeksCari:
            No += 1
            print(f'| {No:>2} | {NIM[i]:9} | {Nama[i]:20} | {NA[i]:>5.1f} |')
    if No == 0:
        print(f'Indeks {IndeksCari} Tidak Ditemukan!')
    print('----------------------------------------------------------')

# Badan program utama
os.system('cls')
# Penciptaan array NIM, nama mahasiswa (Nama), nilai akhir (NA) dan Indeks
NIM = ['/'] * MAKSMHS
Nama = ['/'] * MAKSMHS
NA = [0] * MAKSMHS
Indeks = ['/'] * MAKSMHS

# Memasukkan kelas dan nama mata kuliah
print('<<PENGISIAN DATA NILAI MAHASISWA>>')
Kelas = str(input('Kelas       : '))
MatKul = str(input('Mata Kuliah : '))
N = IsiDataMhs(NIM, Nama, NA, Indeks)

os.system('cls')
# Memanggil subrutin tampil data nilai
print('<<ISI ARRAY NILAI MAHASISWA>>')
TampilDataMhs(NIM, Nama, NA, Indeks, Kelas, MatKul, N)
os.system('pause')

Lagi = 'Y'
while Lagi != 'T':
    os.system('cls')
    print('Menu Pencarian')
    print('--------------')
    print('1. Cari NIM')
    print('2. Cari Nilai Akhir')
    print('3. Cari Indeks Nilai')
    Pilih = int(input('Pilihan Anda? '))
    os.system('cls')
    match Pilih:
        case 1:  # binary search terhadap NIM
            print('<<PENCARIAN NIM TERTENTU>>')
            UrutNIMAsc(NIM, Nama, NA, Indeks, N)
            CariNIM(NIM, Nama, NA, Indeks, N)

        case 2:  # sequential search terhadap Nilai Akhir
            print('<<PENCARIAN NILAI AKHIR TERTENTU>>')
            CariNilai(NIM, Nama, NA, Indeks, N)

        case 3:  # sequential search terhadap Indeks
            print('<<PENCARIAN INDEKS NILAI TERTENTU>>')
            CariIndeks(NIM, Nama, NA, Indeks, N)

    print()
    Lagi = str(input('Mau Coba Lagi [Y/T]? ')).upper()