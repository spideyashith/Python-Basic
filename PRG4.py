import array as arr

# ------------------ MEAN ------------------
a = arr.array('i', [1, 2, 8, 9, 4])
total = 0

for i in a:
    total += i

mean = total / len(a)
print("The Mean:", mean)

print("----------------------------------------------------------------")

# ------------------ MEDIAN ------------------
a = sorted(a)  # Use sorted to avoid changing original array type

n = len(a)
if n % 2 == 0:
    median = (a[n // 2 - 1] + a[n // 2]) / 2
else:
    median = a[n // 2]

print("The Median:", median)

print("----------------------------------------------------------------")

# ------------------ STANDARD DEVIATION ------------------
# Step 1: Calculate mean
mean = sum(a) / len(a)

# Step 2: Find squared differences from mean
squared_diff = [(x - mean) ** 2 for x in a]

# Step 3: Calculate variance (sample)
variance = sum(squared_diff) / (len(a) - 1)

# Step 4: Take square root for standard deviation
sd = variance ** 0.5

print("Standard Deviation:", sd)
