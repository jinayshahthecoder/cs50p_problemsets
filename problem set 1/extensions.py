# Problem Set 1 Question 3
# To output the media type of the file whose name and extension have been entered

# Get user input of file ande split it into two parts
filename, extension = input("File name: ").lower().strip().split(".")

# Use match-case conditional to print the final answer
match extension:
    case "gif":
        print("image/gif")
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case "txt":
        print("text/plain")
    case _:
        print("application/octect-stream")