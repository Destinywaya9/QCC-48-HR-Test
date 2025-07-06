from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "QCC demo is active!"}

class InputData(BaseModel):
    signal_strength: float
    coherence_factor: float

@app.post("/simulate")
def simulate(data: InputData):
    entropy_baseline = 100
    effective_resonance = data.signal_strength * data.coherence_factor
    entropy_reduction = effective_resonance * 0.75
    result = entropy_baseline - entropy_reduction
    return {
        "result": round(result, 2),
        "status": "Simulation complete",
        "resonance_effect": round(effective_resonance, 2)
    }
