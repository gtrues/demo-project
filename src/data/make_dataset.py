import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate demo data
n_samples = 100
data = {
    'id': range(1, n_samples + 1),
    'age': np.random.randint(18, 65, size=n_samples),
    'income': np.random.normal(50000, 15000, size=n_samples).astype(int),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], size=n_samples),
    'purchased': np.random.choice([0, 1], size=n_samples)
}

df = pd.DataFrame(data)

# Save to CSV
output_path = 'data/demo_data.csv'
df.to_csv(output_path, index=False)

print(f"Demo data saved to {output_path}")