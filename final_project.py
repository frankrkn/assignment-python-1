print("Select how you wish to proceed.")
print("Type 'text' to enter plain text.")
print("Type 'file' to specify file directory.")

input_mode = input("Your choice:").strip().lower()

if input_mode == "text":
  text = input("Please enter your text:\n")

elif input_mode == "file":
  file_path = input("Please specify the directory of your .txt file: ")

else:
  print("Invalid choice, please restart the program.")
  exit()