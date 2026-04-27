# model_serving

Proyecto sencillo de **FastAPI** para servir un modelo de Machine Learning.

## Estructura

```
model_serving/
├── main.py            # FastAPI: endpoint /predict
├── models/            # aquí pondremos el pickle más adelante
├── pyproject.toml
└── README.md
```

## Instalación

Este proyecto usa [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Ejecución

```bash
uv run uvicorn main:app --reload
```

API en `http://127.0.0.1:8000` y documentación interactiva en `http://127.0.0.1:8000/docs`.

## Endpoint

`POST /predict/` — recibe un batch de observaciones y devuelve la predicción.

```bash
curl -X POST http://127.0.0.1:8000/predict/ \
  -H "Content-Type: application/json" \
  -d '{"X": [[5.1, 3.5, 1.4, 0.2]]}'
```
