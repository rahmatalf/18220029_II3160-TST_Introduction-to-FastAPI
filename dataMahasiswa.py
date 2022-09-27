import json
from fastapi import FastAPI, HTTPException

with open("dataMahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/dataMahasiswa/{item_nim}')
async def read_mahasiswa(item_nim: int):
    for mahasiswa in data['dataMahasiswa']:
        if mahasiswa['nim'] == item_nim:
            return mahasiswa

raise HTTPException(
    status_code=404, detail=f'Item not found'
)