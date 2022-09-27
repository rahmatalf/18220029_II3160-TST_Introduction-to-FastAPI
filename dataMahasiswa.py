from http.client import HTTPException
import json
from fastapi import FastAPI

with open("dataMahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()
listMahasiswa = []

@app.get('/dataMahasiswa/{item_id}')
async def create_listMahasiswa():
    for mahasiswa in data['dataMahasiswa']:
        dictMahasiswa = {'NIM': mahasiswa['nim'], 'Nama': mahasiswa['nama']}
        listMahasiswa.append(dictMahasiswa)

raise HTTPException(
    status_code=404, detail=f'Item not found'
)