with open("HYY.txt","r") as f1, open("Hello.txt","r") as f2, open("1HELLO.txt","w") as f3:
           f3.write(f1.read())
           f3.write("\n")
           f3.write(f2.read())
           
           
print("Files merged successfully!")