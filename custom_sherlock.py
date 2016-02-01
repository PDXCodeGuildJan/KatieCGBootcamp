"""A program to make a custom version of The Adventures of Sherlock Holmes,
   by replacing all instances of "Sherlock" with a user's input."""

__author__ = "Katie"

import re

def main():
   """Get a name from the user and then replace every instance 
      of "Sherlock" with the  given name."""

   # Welcome the users to the generator
   print("Sherlock Adventure Generator")
   print("-------------------------------------\n\n")

   # Prompt them for the name to use in the new version of the story
   test = input("Who do you wish to explore London with Dr. John Watson?> ")
   print(test)

   # Open the original story and grab all of the text.
   old_file = open("Sherlock_Holmes.txt", "r")
   old_text = old_file.read()
   old_file.close()

   # Swap out all instances of Sherlock with the new name
   # First, replace any all-caps versions of Sherlock with 
   #     an all-caps version of the new name.
   new_text = re.sub("SHERLOCK", new_name.upper(), old_text)

   # Then, replace all 'normal' versions of Sherlock with 
   #     'normal' versions of the new name.
   new_text = re.sub("Sherlock", new_name, new_text)

   # Write the new version of the story to a new file.
   file_name = "The_Adventures_of_" + new_name + "_Holmes.txt"
   new_file = open(file_name, "w")
   new_file.write(new_text)
   new_file.close()

   # Tell the user we're done!
   print("Congratulations! The Adventures of", new_name, 
         "Holmes has been written to", file_name, "\n")
   print("Please remember that if you picked a female name, "
         "the book will still refer to them as a 'he'.\n\n\n")


   # Fin :D


if __name__ == '__main__':
   main()