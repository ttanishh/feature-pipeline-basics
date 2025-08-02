from feature_engine.imputation import CategoricalImputer, MeanMedianImputer
from feature_engine.encoding import OneHotEncoder
from sklearn.pipeline import Pipeline

def build_pipeline():
    pipeline = Pipeline(steps=[
        ("categorical_imputer", CategoricalImputer(imputation_method="frequent")),
        ("numerical_imputer", MeanMedianImputer(imputation_method="mean")),
        ("categorical_encoder", OneHotEncoder(drop_last=True))  # Optional: drop_last to avoid dummy trap
    ])
    return pipeline
