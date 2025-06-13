import pandas as pd

# Given dataset
data = [
    ("rainy", "hot", "high", "false", "no"),
    ("rainy", "hot", "high", "true", "no"),
    ("overcast", "hot", "high", "false", "yes"),
    ("sunny", "mild", "high", "false", "yes"),
    ("sunny", "cool", "normal", "false", "yes"),
    ("sunny", "cool", "normal", "true", "no"),
    ("overcast", "cool", "normal", "true", "yes"),
    ("rainy", "mild", "high", "false", "no"),
    ("rainy", "cool", "normal", "false", "yes"),
    ("sunny", "mild", "normal", "false", "yes"),
    ("rainy", "mild", "normal", "true", "yes"),
    ("overcast", "mild", "high", "true", "yes"),
    ("overcast", "hot", "normal", "false", "yes"),
    ("sunny", "mild", "high", "true", "no"),
]

df = pd.DataFrame(data, columns=["outlook", "temperature", "humidity", "windy", "play"])

# Count occurrences of "yes" and "no"
yes_count = df["play"].value_counts()["yes"]
no_count = df["play"].value_counts()["no"]
total_count = len(df)

# Prior probabilities
P_yes = yes_count / total_count
P_no = no_count / total_count

print(f"P(yes) = {P_yes:.4f}, P(no) = {P_no:.4f}")

# Function to compute likelihood with Laplace Smoothing
def likelihood_smooth(attribute, value, play_value, alpha=1):
    subset = df[df["play"] == play_value]
    count_value = len(subset[subset[attribute] == value]) + alpha  
    count_total = len(subset) + alpha * len(df[attribute].unique())  
    return count_value / count_total

# Compute likelihoods
attributes = [("outlook", "rainy"), ("temperature", "hot"), ("humidity", "high"), ("windy", "false")]
P_given_yes = 1
P_given_no = 1

for attr, val in attributes:
    P_attr_yes = likelihood_smooth(attr, val, "yes")
    P_attr_no = likelihood_smooth(attr, val, "no")
    print(f"P({val} | yes) = {P_attr_yes:.4f}, P({val} | no) = {P_attr_no:.4f}")
    P_given_yes *= P_attr_yes
    P_given_no *= P_attr_no

# Compute final probabilities
P_yes_given_data = P_given_yes * P_yes
P_no_given_data = P_given_no * P_no

# Normalize
P_total = P_yes_given_data + P_no_given_data
P_yes_given_data /= P_total
P_no_given_data /= P_total

# Final Prediction
prediction_corrected = "yes" if P_yes_given_data > P_no_given_data else "no"

print(f"P(yes | data) = {P_yes_given_data:.4f}")
print(f"P(no | data) = {P_no_given_data:.4f}")
print(f"Prediction: {prediction_corrected}")
