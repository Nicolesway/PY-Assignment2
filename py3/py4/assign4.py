def file_read_write():
    # Ask user for input filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file for reading
        file = open('input.txt', 'r') 
        content = file.read()
        

        # Modify the content (make everything uppercase)
        modified_content = content.upper()
        

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
         new_file.write("modified_content")
        print(modified_content)

        print(f"File successfully modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
        
file_read_write()

    




