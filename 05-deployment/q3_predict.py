from __future__ import annotations

import pickle
from pathlib import Path

from model import normalize_record


MODEL_PATH = Path(__file__).with_name("pipeline.bin")
LEAD = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

with MODEL_PATH.open("rb") as model_file:
    pipeline = pickle.load(model_file)

probability = float(pipeline.predict_proba([normalize_record(LEAD)])[0, 1])
print(f"conversion_probability: {probability:.6f} (rounded: {probability:.3f})")
