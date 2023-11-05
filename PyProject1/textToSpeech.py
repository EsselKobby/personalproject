from gtts import gTTS
import os

tts = gTTS("hello")

tts.save("vlc hello.mp3")
os.system("hello.mp3")

# Variable Declaration
place = input("Place: ")
adjective = input("Adjective: ")
animal = input("Animal: ")
name = input("Name: ")
verb = input("Verb: ")
food = input("Food: ")

# Defined the story with placeholders
story = f"""Once upon a time, in a faraway {place}, there lived a {adjective} {animal}. This {animal} had a best friend named {name}. They loved to {verb} together and always had {food} for lunch."""

# Print the completed story
print(story)

# Text to Speech
tts = gTTS(text=story, lang="en")
tts.save("story.mp3")
os.system("vlc story.mp3")
