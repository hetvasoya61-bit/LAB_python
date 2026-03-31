"""#1.write()
f=open("one.txt","w")
f.write("hello student\n")
f.write("welcome to python file handling.\n")
f.write("learning is fun!\n")
f.close()"""

"""#2.writelines()
f=open("one.txt","w")
lines=[
    "python programming\n",
    "file handling\n",
    "error handling\n",
    "exception handling\n"
]
f.writelines(lines)
f.close()"""

"""#3.append()
f=open("one.txt","a")
lines=[
    "python programming\n",
    "file handling\n",
    "error handling\n",
    "exception handling\n"
]
f.writelines(lines)
f.close()"""

