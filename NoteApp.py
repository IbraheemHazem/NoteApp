# Set the file path for storing notes
file_path = "notes.txt"

# Display welcome messages
print("---------------------------------------------------------")
print("---------------- Welcome to YourNote app ----------------")
print("---------------------------------------------------------")

# Main loop for the note app
while True:
    # Ask the user for their command choice
    choice = input("Do you want to (add/view/delete/exit) the program?\nChoose a command:")

    if choice == "add":
        # If the user chooses to add a note
        task = input("Enter your new note:").strip()
        with open(file_path, "a") as WriteNotes:
            # Write the new note to the file
            print(task, file=WriteNotes)
            print("Note added successfully!")

    elif choice == "view":
        # If the user chooses to view notes
        with open(file_path, "r") as ReadNotes:
            # Display each note to the user
            for view in ReadNotes:
                print(view.strip())

    elif choice == "delete":
        # If the user chooses to delete a note
        deleted_msg = input("Enter the note you want to delete:").strip()
        with open(file_path, "r") as ReadNotes:
            # Read all notes from the file
            Notes = ReadNotes.readlines()

        if deleted_msg in [note.strip() for note in Notes]:
            # If the note to delete is found, update the file
            with open(file_path, "w") as DeleteNotes:
                for line in Notes:
                    if line.strip() != deleted_msg:
                        # Write all notes except the one to be deleted
                        print(line.strip(), file=DeleteNotes)
                print(f"Note '{deleted_msg}' deleted successfully.")
        else:
            # If the note to delete is not found, inform the user
            print(f"Note '{deleted_msg}' not found.")

    elif choice == "exit":
        # If the user chooses to exit, break the loop
        print("App Closed successfully!")
        break
    else:
        # If the user enters an invalid command, prompt again
        print("Invalid Command, Please type 'add', 'view', 'delete', or 'exit'.")
