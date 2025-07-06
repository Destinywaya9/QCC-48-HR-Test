from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "QCC demo is active!"}

class SimulationInput(BaseModel):
    signal_strength: float
    coherence_factor: float

@app.post("/simulate")
def simulate_qcc(input: SimulationInput):
    # Basic mock logic for QCC signal resonance
    resonance_effect = input.signal_strength * input.coherence_factor
    result = round((resonance_effect + random.uniform(-1.5, 1.5)) * 10, 2)
    return {
        "status": "Simulation complete",
        "resonance_effect": round(resonance_effect, 2),
        "result": result
    }
