## EXAMPLE SERVE GPT MODEL with FASTAPI and STREAMLIT

### 1. Download Pretrained Model

[Google Drive](https://drive.google.com/drive/folders/11aWe3IZ0pfxujwzsFHwSzgJuAlPryBNs)

Extract and put baseline folder into:
```
/API/server/gpt/pretrained_model
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Run
```bash
python API/main.py & streamlit run UI/app.py --server.port 8000
```

### 4. Change port (Optional)

for API, change port in `API/main.py`
for UI, change __--server.port above__