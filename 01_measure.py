"""
Calculate share of variance from each data point
"""

# load necessary modules
import pandas as pd

# load necessary data
data = {"id": list(range(10)),
        "num_pets": [0, 1, 1, 2, 1, 3, 0, 0, 10, 0]}

pets_df = pd.DataFrame(data=data)

# store mean and variance
mean_pets = pets_df["num_pets"].mean()
variance_pets = pets_df["num_pets"].var()

# view results
print(f"The mean number of pets is {mean_pets}")

# calculate variance for each data point
pets_df["variance"] = pets_df["num_pets"] - mean_pets

# calculate squared deviation
pets_df["squared_dev_pets"] = pets_df["variance"] ** 2

# share of variance per data point
pets_df["share_of_total_variance"] = pets_df["squared_dev_pets"] / pets_df["squared_dev_pets"].sum()

# view results
print(pets_df)
print(f"The total share of variance sums up to {pets_df['share_of_total_variance'].sum()}")

# end of script #
