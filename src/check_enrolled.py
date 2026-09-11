import pickle

with open("models/encodings.pkl", "rb") as f:
    data = pickle.load(f)

print("Enrolled people:", data.get("names", []))
print("Total encodings:", len(data.get("encodings", [])))
