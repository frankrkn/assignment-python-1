print("Select how you wish to proceed.")
print("Type 'text' to enter plain text.")
print("Type 'file' to specify file directory.")

input_mode = input("Your choice:").strip().lower() ##Strips words from the sentence by using spaces inbetween and lowercases all characters.

if input_mode == "text":
  text = input("Please enter your text:\n")

elif input_mode == "file":
  file_path = input("Please specify the directory of your .txt file: ")

else:
  print("Invalid choice, please restart the program.")
  exit()

if input_mode == "file":
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    
    except FileNotFoundError:
        print("File not found, please try again.")
        file_path = input("Please enter the .txt file path correctly.")
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
              text = file.read()
        
        except FileNotFoundError:
            print("Unable to find requested file in specified directory, shutting down the program")
            exit()
            
clean_text = text.lower()
new_text = ""

for char in clean_text:
  if char.isalpha() or char.isspace():
    new_text = new_text + char

clean_text = new_text
words = clean_text.split()

show_characters = input("Would you like to see total amount of characters? Please answer 'yes' or 'no'.").strip().lower()
show_words = input("Would you like to see total amount of words? Please answer 'yes' or 'no'.").strip().lower()

if show_characters == "yes":
  character_count = len(text)
  print("Total number of characters", character_count)

if show_words == "yes":
  word_count = len(words)
  print("Total number of words", word_count)
  
stopwords = {"the", "and", "is", "to", "of", "in", "that", "on", "for", "with"}
word_freq = {}

for word in words:
    if word not in stopwords:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        
        else:
            word_freq[word] = 1
            
##I will use three example texts pulled directly online, topic detection will be limited to those texts. I'd have liked to go for a more accurate value driven keyword strategies
##but that sounds like a semester long project to hone it instead of a few weeks long.

topics = {
    "data_science_python": [
        "python", "data", "science", "machine", "learning", "ai",
        "analytics", "libraries", "pandas", "numpy", "model",
        "dataset", "algorithm", "statistics", "automation", "career"
    ],

    "wildlife_conservation": [
        "snow", "leopard", "wildlife", "conservation", "species",
        "population", "habitat", "ecosystem", "endangered",
        "protection", "biodiversity", "monitoring", "research",
        "mountain", "community"
    ],

    "digestive_health": [
        "digestive", "digestion", "stomach", "intestine",
        "nutrients", "absorption", "gut", "bacteria",
        "fibre", "diet", "nutrition", "hydration",
        "water", "exercise", "health"
    ]
}

topic_scores = {}

for topic in topics:
  topic_scores[topic] = 0

for word in word_freq:
  for topic in topic_scores:
    if word in topics[topic]:
      topic_scores[topic] = topic_scores[topic] + word_freq[word]

detected_topic = max(topic_scores, key=topic_scores.get)

print("Detected topic is:", detected_topic)