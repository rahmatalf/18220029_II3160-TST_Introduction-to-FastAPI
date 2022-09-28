import json
import string
from fastapi import FastAPI

with open("dataMahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

# Kelas Mahasiswa
class Mahasiswa:
    nama: string
    fakultas: string
    jurusan: string 

    def __init__(self, nama, fakultas, jurusan):
        self.nama = nama
        self.fakultas = fakultas
        self.jurusan = jurusan

n = int(input("Jumlah Mahasiswa: "))
for i in range (n-1):
    print("Mahasiswa ke-" + n)
    nim      = int(input("NIM     : "))
    nama     = input("Nama    :")
    fakultas = input("Fakultas:")
    jurusan  = input("Jurusan :")
    mahasiswa = Mahasiswa(nama, fakultas, jurusan)
 
@app.get('/dataMahasiswa/{item}')
async def get_listMahasiswa():
    for mahasiswa in data['dataMahasiswa']:
        dictMahasiswa = {'NIM': mahasiswa['nim'], 'Nama': mahasiswa['nama']}
        listMahasiswa.append(dictMahasiswa)
    return listMahasiswa