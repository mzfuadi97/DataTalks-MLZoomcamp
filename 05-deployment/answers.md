# Jawaban Homework 5 — Deploying ML Models

Artifact check: `sha256sum pipeline.bin` →
`1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1` (sesuai).

| No | Jawaban | Cara mendapatkan |
| --- | --- | --- |
| Q1 | `uv 0.12.19` (catatan saja, tidak dinilai) | `uv --version` |
| Q2 | **`1.7.2`** | `pyproject.toml` / `uv.lock` (`scikit-learn==1.7.2`) |
| Q3 | **`0.533`** (0.532994) | `uv run python q3_predict.py` |
| Q4 | **`0.770`** (0.769799, `conversion: true`) | `uv run uvicorn predict:app --port 9696` + `python q6_test.py` |
| Q5 | **`python:3.11.15-slim-bookworm`** | baris `FROM` di `Dockerfile` |
| Q6 | **`0.770`** (0.769799 dari container, `conversion: true`) | `docker run -p 9696:9696 zoomcamp-model:2026-hw5` + `python q6_test.py` |

`GET /health` mengembalikan `{"status":"ok","model_sha256":"1646bbdc...29f1", ...}`,
sama dengan `model_sha256` di `model_metadata.json`.

## Langkah

```bash
uv sync --locked
uv run python smoke_test.py
uv run python q3_predict.py                      # Q3
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
python q6_test.py                                # Q4 (terminal lain)

docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
python q6_test.py                                # Q6
curl -s http://localhost:9696/health
```
