import pickle

with open("dataset/notes.pkl", "rb") as f:
    notes = pickle.load(f)

print("Total Notes:", len(notes))
print("First 50 Notes:")
print(notes[:50])