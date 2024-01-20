# Geting user input
file_1 = input("File Name: ").lower().strip()
# conditions
if ".gif" in file_1:
    print("image/gif")
elif ".pdf" in file_1:
    print("application/pdf")
elif ".jpg" in file_1:
    print("image/jpeg")
elif ".jpeg" in file_1:
    print("image/jpeg")
elif ".png" in file_1:
    print("image/png")
elif ".txt" in file_1:
    print("text/plain")
elif ".zip" in file_1:
    print("application/zip")
else:
    print("application/octet-stream")