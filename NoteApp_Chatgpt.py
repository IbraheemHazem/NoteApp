# def add_note(notes):
#     new_note = input("Enter your new note: ")
#     notes.append(new_note)
#     print("Note added successfully.")

# def view_notes(notes):
#     if notes:
#         print("Your Notes:")
#         for i, note in enumerate(notes, 1):
#             print(f"{i}. {note}")
#     else:
#         print("No notes found.")

# #note1
# def delete_note(notes):
#     if notes:
#         view_notes(notes)
#         note_index = int(input("Enter the number of the note you want to delete: "))
#         if 1 <= note_index <= len(notes):
#             deleted_note = notes.pop(note_index - 1)
#             print(f"Deleted note: {deleted_note}")
#         else:
#             print("Invalid note number.")
#     else:
#         print("No notes found.")

# #note2
# def delete_note(notes):
#     if notes:
#         view_notes(notes)
#         try:
#             note_index = int(input("Enter the number of the note you want to delete (0 to cancel): "))
#             if 1 <= note_index <= len(notes):
#                 deleted_note = notes.pop(note_index - 1)
#                 print(f"Deleted note: {deleted_note}")
#             elif note_index == 0:
#                 print("Delete operation canceled.")
#             else:
#                 print("Invalid note number.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#     else:
#         print("No notes found.")

##note3
# def delete_note(notes):
#     if notes:
#         view_notes(notes)
#         try:
#             note_index = int(input("Enter the number of the note you want to modify (0 to cancel): "))
#             if 1 <= note_index <= len(notes):
#                 modified_note = input(f"Modify the note: {notes[note_index - 1]}\nEnter the modified note: ")
#                 notes[note_index - 1] = modified_note
#                 print("Note modified successfully.")
#             elif note_index == 0:
#                 print("Modification canceled.")
#             else:
#                 print("Invalid note number.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#     else:
#         print("No notes found.")


# Main program
# notes = []

# while True:
#     print("\nOptions:")
#     print("1. Add Note")
#     print("2. View Notes")
#     print("3. Delete Note")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         add_note(notes)
#     elif choice == "2":
#         view_notes(notes)
#     elif choice == "3":
#         delete_note(notes)
#     elif choice == "4":
#         print("Exiting the Note App. Goodbye!")
#         break
#     else:
#         print("Invalid option. Please enter 1, 2, 3, or 4.")




















# import os

# def create_note():
#     # Get user input for the note
#     note_content = input("Write your note: ")

#     # Save the note to a file
#     with open("notes.txt", "a") as file:
#         file.write(note_content + "\n")
    
#     print("Note saved successfully!")

# def view_notes():
#     try:
#         # Read and display existing notes from the file
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()

#         if notes:
#             print("Your Notes:")
#             for i, note in enumerate(notes, start=1):
#                 print(f"{i}. {note.strip()}")
#         else:
#             print("No notes available.")
#     except FileNotFoundError:
#         print("No notes available.")

# def delete_note():
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()

#         if notes:
#             print("Your Notes:")
#             for i, note in enumerate(notes, start=1):
#                 print(f"{i}. {note.strip()}")

#             choice = int(input("Enter the number of the note you want to delete: "))

#             if 1 <= choice <= len(notes):
#                 del notes[choice - 1]

#                 with open("notes.txt", "w") as file:
#                     file.writelines(notes)

#                 print("Note deleted successfully!")
#             else:
#                 print("Invalid note number. Please enter a valid number.")
#         else:
#             print("No notes available.")
#     except FileNotFoundError:
#         print("No notes available.")

# # Main loop
# while True:
#     print("\nOptions:")
#     print("1. Create a new note")
#     print("2. View notes")
#     print("3. Delete a note")
#     print("4. Exit")

#     choice = input("Enter your choice (1, 2, 3, or 4): ")

#     if choice == '1':
#         create_note()
#     elif choice == '2':
#         view_notes()
#     elif choice == '3':
#         delete_note()
#     elif choice == '4':
#         print("Exiting the note-taking app. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter 1, 2, 3, or 4.")


















#if we want to modify the note manually
# def write_to_file(file_path, notes):
#     with open("notes.txt", "w") as file:
#         file.writelines(notes)

# def show_notes(notes):
#     if notes:
#         print("Your Notes:")
#         for i, note in enumerate(notes, 1):
#             print(f"{i}. {note.strip()}")
#     else:
#         print("No notes found.")

# def add_note(notes):
#     new_note = input("Enter your new note: ")
#     notes.append(new_note + "\n")
#     print("Note added successfully.")
#     write_to_file("notes.txt", notes)  # Write updated notes to the file

# def delete_note(notes):
#     if notes:
#         show_notes(notes)
#         try:
#             note_index = int(input("Enter the number of the note you want to modify (0 to cancel): "))
#             if 1 <= note_index <= len(notes):
#                 modified_note = input(f"Modify the note: {notes[note_index - 1]}\nEnter the modified note: ")
#                 notes[note_index - 1] = modified_note + "\n"
#                 print("Note modified successfully.")
#                 write_to_file("notes.txt", notes)  # Write updated notes to the file
#             elif note_index == 0:
#                 print("Modification canceled.")
#             else:
#                 print("Invalid note number.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#     else:
#         print("No notes found.")

# # Main loop
# notes = []

# while True:
#     print("\nOptions:")
#     print("1. Show Notes")
#     print("2. Add Note")
#     print("3. Modify Note")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         show_notes(notes)
#     elif choice == "2":
#         add_note(notes)
#     elif choice == "3":
#         delete_note(notes)
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")









##if we want to enter the number or the note itself
# def write_to_file(file_path, notes):
#     with open(file_path, "w") as file:
#         file.writelines(notes)

# def show_notes(notes):
#     if notes:
#         print("Your Notes:")
#         for i, note in enumerate(notes, 1):
#             print(f"{i}. {note.strip()}")
#     else:
#         print("No notes found.")

# def add_note(notes):
#     new_note = input("Enter your new note: ")
#     notes.append(new_note + "\n")
#     print("Note added successfully.")
#     write_to_file("notes.txt", notes)  # Write updated notes to the file

# def delete_note(notes):
#     if notes:
#         show_notes(notes)
#         try:
#             note_input = input("Enter the number of the note you want to modify or enter the modified note directly: ")
#             if note_input.isdigit():
#                 note_index = int(note_input)
#                 if 1 <= note_index <= len(notes):
#                     modified_note = input(f"Modify the note: {notes[note_index - 1]}\nEnter the modified note: ")
#                     notes[note_index - 1] = modified_note + "\n"
#                     print("Note modified successfully.")
#                     write_to_file("notes.txt", notes)  # Write updated notes to the file
#                 else:
#                     print("Invalid note number.")
#             else:
#                 notes.append(note_input + "\n")
#                 print("Note added successfully.")
#                 write_to_file("notes.txt", notes)  # Write updated notes to the file
#         except ValueError:
#             print("Invalid input. Please enter a valid number or note.")
#     else:
#         print("No notes found.")

# # Main loop
# notes = []

# while True:
#     print("\nOptions:")
#     print("1. Show Notes")
#     print("2. Add Note or Modify Note")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3) or enter a note directly: ")

#     if choice.isdigit() and 1 <= int(choice) <= 3:
#         choice = int(choice)
#         if choice == 1:
#             show_notes(notes)
#         elif choice == 2:
#             delete_note(notes)
#         elif choice == 3:
#             break
#     else:
#         add_note(notes)











# def add_note(file_path, new_note):
#     with open(file_path, "a") as file:
#         file.write(new_note + "\n")
#     print("Note added successfully!")

# def view_notes(file_path):
#     try:
#         with open(file_path, "r") as file:
#             notes = file.readlines()
#             if notes:
#                 print("Your Notes:")
#                 for i, note in enumerate(notes, 1):
#                     print(f"{i}. {note.strip()}")
#             else:
#                 print("No notes found.")
#     except FileNotFoundError:
#         print("File not found.")

# def delete_note(file_path, note_to_delete):
#     try:
#         with open(file_path, "r") as file:
#             notes = file.readlines()

#         if note_to_delete in notes:
#             notes.remove(note_to_delete)

#             with open(file_path, "w") as file:
#                 file.writelines(notes)

#             print(f"Note '{note_to_delete}' deleted successfully.")
#         else:
#             print(f"Note '{note_to_delete}' not found.")
#     except FileNotFoundError:
#         print("File not found.")

# def main():
#     file_path = "notes.txt"

#     print("************** Welcome to YourNote app **************")

#     while True:
#         choice = input("Do you want to (add/view/delete/exit) the program?\nChoose a command:")

#         if choice == "add":
#             task = input("Enter your new note:\n").rstrip()
#             add_note(file_path, task)

#         elif choice == "view":
#             view_notes(file_path)

#         elif choice == "delete":
#             deleted_msg = input("Enter the note you want to delete:").rstrip()
#             delete_note(file_path, deleted_msg)

#         elif choice == "exit":
#             print("App Closed successfully")
#             break

#         else:
#             print("Invalid Command, Please type 'add', 'view', 'delete', or 'exit'.")
#             print(40 * "*")

# if __name__ == "__main__":
#     main()







# file_path = "notes.txt"

# def add_note():
#     task = input("Enter your new note:\n").strip()
#     with open(file_path, "a") as WriteNotes:
#         print(task, file=WriteNotes)
#         print("Note added successfully!")

# def view_notes():
#     with open(file_path, "r") as ReadNotes:
#         for view in ReadNotes:
#             print(view.strip())

# def delete_note():
#     deleted_msg = input("Enter the note you want to delete:").strip()
#     with open(file_path, "r") as ReadNotes:
#         Notes = ReadNotes.readlines()

#     if deleted_msg in [note.strip() for note in Notes]:
#         with open(file_path, "w") as DeleteNotes:
#             for line in Notes:
#                 if line.strip() != deleted_msg:
#                     print(line.strip(), file=DeleteNotes)
#             print(f"Note '{deleted_msg}' deleted successfully.")
#     else:
#         print(f"Note '{deleted_msg}' not found.")

# print("---------------------------------------------------------")
# print("---------------- Welcome to YourNote app ----------------")
# print("---------------------------------------------------------")

# while True:
#     choice = input("Do you want to (add/view/delete/exit) the program?\nChoose a command:")

#     if choice == "add":
#         add_note()

#     elif choice == "view":
#         view_notes()

#     elif choice == "delete":
#         delete_note()

#     elif choice == "exit":
#         print("App Closed successfully!")
#         break

#     else:
#         print("Invalid Command, Please type 'add', 'view', 'delete', or 'exit'.")




# file_path = "notes.txt"

# def add_note():
#     [print(input("Enter your new note:\n").strip(), file=open(file_path, "a")), print("Note added successfully!")]

# def view_notes():
#     [print(line.strip()) for line in open(file_path)]

# def delete_note():
#     deleted_msg = input("Enter the note you want to delete:").strip()
#     [print(line.strip(), file=open(file_path, "w")) for line in open(file_path) if line.strip() != deleted_msg] if deleted_msg in open(file_path).read() else  print(f"Note '{deleted_msg}' not found.")

# print("---------------------------------------------------------")
# print("---------------- Welcome to YourNote app ----------------")
# print("---------------------------------------------------------")

# while True:
#     choice = input("Do you want to (add/view/delete/exit) the program?\nChoose a command:")

#     if choice == "exit":
#         print("App Closed successfully!")
#         break
#     else:
#         add_note() if choice == "add" else (view_notes() if choice == "view" else delete_note() if choice == "delete" else print("Invalid Command, Please type 'add', 'view', 'delete', or 'exit'."))
















# class NoteApp:
#     def __init__(self, file_path="notes.txt"):
#         self.file_path = file_path

#     def add_note(self):
#         task = input("Enter your new note:\n").strip()
#         with open(self.file_path, "a") as file:
#             print(task, file=file)
#         print("Note added successfully!")

#     def view_notes(self):
#         with open(self.file_path, "r") as file:
#             for note in file:
#                 print(note.strip())

#     def delete_note(self):
#         deleted_msg = input("Enter the note you want to delete:").strip()
#         with open(self.file_path, "r") as read_file:
#             notes = read_file.readlines()

#         if deleted_msg in [note.strip() for note in notes]:
#             with open(self.file_path, "w") as write_file:
#                 for line in notes:
#                     if line.strip() != deleted_msg:
#                         print(line.strip(), file=write_file)
#                 print(f"Note '{deleted_msg}' deleted successfully.")
#         else:
#             print(f"Note '{deleted_msg}' not found.")

#     def run(self):
#         print("---------------------------------------------------------")
#         print("---------------- Welcome to YourNote app ----------------")
#         print("---------------------------------------------------------")

#         while True:
#             choice = input("Do you want to (add/view/delete/exit) the program?\nChoose a command:")

#             if choice == "add":
#                 self.add_note()
#             elif choice == "view":
#                 self.view_notes()
#             elif choice == "delete":
#                 self.delete_note()
#             elif choice == "exit":
#                 print("App Closed successfully!")
#                 break
#             else:
#                 print("Invalid Command, Please type 'add', 'view', 'delete', or 'exit'.")


# # Create an instance of the NoteApp class and run the app
# note_app = NoteApp()
# note_app.run()
