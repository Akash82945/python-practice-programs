import numpy as np 


# Normalize Data (0-1 range thinking)

np.random.seed(42)
raw_score = np.random.randint(10,999,5)

score_min = np.min(raw_score)
score_max = np.max(raw_score)

normalized_score = (raw_score - score_min) / (score_max - score_min)
print(f"Original Data : {raw_score}")

formated_data = [f" {x:.2f}" for x in normalized_score]
print(f"Normalized Data : {formated_data}")
