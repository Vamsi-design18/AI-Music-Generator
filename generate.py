import pickle
import random
from music21 import stream, note, chord

# Load notes
with open("dataset/notes.pkl", "rb") as f:
    notes = pickle.load(f)

if not notes:
    print("No notes found!")
    exit()

output_notes = []

for _ in range(500):
    pattern = random.choice(notes)

    try:
        # Chord format: 0.4.7
        if "." in str(pattern):
            notes_in_chord = pattern.split(".")
            chord_notes = []

            for n in notes_in_chord:
                chord_notes.append(note.Note(int(n)))

            output_notes.append(chord.Chord(chord_notes))

        # Numeric values like 10, 11, 7
        elif str(pattern).isdigit():
            continue

        # Normal notes like C4, G#5
        else:
            output_notes.append(note.Note(str(pattern)))

    except Exception:
        continue

# Create MIDI file
midi_stream = stream.Stream(output_notes)
midi_stream.write("midi", fp="generated_music.mid")

print("Music generated successfully!")
print("File saved as generated_music.mid")