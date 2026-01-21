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