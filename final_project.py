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