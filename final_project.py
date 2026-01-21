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
##I have broadened the detection

def display_topic_scores(topic_scores):##Forgot I need to show topic scores and keywords as output, as well as having forgotten that I need a sorting technique in the code
  print("\nTopic Scores:")             ##this code solves both of the issues.
  for topic in topic_scores:
    print(topic + ": " + str(topic_scores[topic]))

def display_top_keyword(word_freq, topics, detected_topic, top_n=3):
  print("\nTop keywords for detected topic (" + detected_topic + ") :")

  used = {}
  for word in topics[detected_topic]:
    if word in word_freq:
      used[word] = word_freq[word]

  sorted_used = []
  while used:
    max_word = None
    max_count = -1

    for word in used:
      if used[word] > max_count:
        max_count = used[word]
        max_word = word
  
    if max_word:
      sorted_used.append((max_word, max_count))
      del used[max_word]

  for i in range(min(top_n, len(sorted_used))):
    word, count = sorted_used[i]
  
  print(word + ": " + str(count))

topics = {
    "technology": [
        "technology", "data", "science", "computer", "programming",
        "ai", "machine", "model", "algorithm", "software", "system"
    ],

    "environment": [
        "nature", "wild", "environment", "animal", "species",
        "habitat", "conservation", "ecosystem", "population",
        "forest", "climate", "sustainability"
    ],

    "health": [
        "health", "body", "nutrition", "food", "exercise",
        "digestive", "wellness", "disease", "nutrients", "water",
        "lifestyle", "immune"
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

display_topic_scores(topic_scores)
display_top_keyword(word_freq, topics, detected_topic)

print("Detected topic is:", detected_topic)