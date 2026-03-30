src=open("Hello.txt","r")
data = src.read()
src.close()

dst = open("Hii.txt","w")
dst.write(data)
dst.close()
print("File copied successfully.")
