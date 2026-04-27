from typing import Any

from fastapi import FastAPI

app = FastAPI()

model = None  # más adelante cargaremos aquí el modelo desde un pickle


@app.post("/predict/")
async def predict(data: dict[str, Any]):
    # data es el JSON que llega en el body, ya parseado a diccionario
    return {"y_pred": "default", "confidence": 0.7}
