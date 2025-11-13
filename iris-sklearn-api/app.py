# app.py
from fastapi import FastAPI
from pydantic import BaseModel, conlist
import joblib
import numpy as np

MODEL_PATH = "model.joblib"

app = FastAPI(title="Iris Sklearn Inference API")

# 加载模型（实际生产可以加异常处理 / 热更新等）
model = joblib.load(MODEL_PATH)

class IrisInput(BaseModel):
    # 单个样本：4维特征
    features: conlist(float, min_length=4, max_length=4)

class IrisBatchInput(BaseModel):
    # 批量样本
    batch: list[conlist(float, min_length=4, max_length=4)]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(input_data: IrisInput):
    X = np.array(input_data.features).reshape(1, -1)
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0].tolist()
    return {
        "prediction": int(pred),
        "probabilities": proba
    }

@app.post("/predict_batch")
def predict_batch(input_data: IrisBatchInput):
    X = np.array(input_data.batch)
    preds = model.predict(X).tolist()
    probas = model.predict_proba(X).tolist()
    return {
        "predictions": [int(p) for p in preds],
        "probabilities": probas
    }