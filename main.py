import pandas as pd
from pipeline.pipeline_feature import build_pipeline, save_pipeline

# Load dataset
df = pd.read_csv("data/dataset.csv")

# OPTIONAL: Print missing value info
print("Missing values per column:\n", df.isnull().sum())

# Build pipeline
pipeline = build_pipeline()

# Fit and transform the data
transformed_data = pipeline.fit_transform(df)

# Save pipeline
save_pipeline(pipeline)

# Display output
print("Transformed Data Sample:")
print(transformed_data[:5])
