def copy_file(source_file, dest_file, convert_to):
    try:
        with open(source_file, 'r') as source:
            data = source.read()
            if convert_to.lower() == 'upper':
                data = data.upper()
            elif convert_to.lower() == 'lower':
                data = data.lower()
            else:
                print("Invalid choice for conversion. Please enter 'upper' or 'lower'.")
                return
            
            with open(dest_file, 'w') as dest:
                dest.write(data)
            print(f"Contents copied from '{source_file}' to '{dest_file}' after converting to {convert_to} case.")
    except FileNotFoundError:
        print("File not found. Please check the file names and paths.")

def main():
    source_file = input("Enter the source file name: ")
    dest_file = input("Enter the destination file name: ")
    convert_to = input("Enter 'upper' or 'lower' to convert text to that case: ")

    copy_file(source_file, dest_file, convert_to)

if __name__ == "__main__":
    main()
