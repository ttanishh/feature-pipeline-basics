from .transformer import build_pipeline
import joblib

def save_pipeline(pipeline, filename="pipeline.joblib"):
    joblib.dump(pipeline, filename)
