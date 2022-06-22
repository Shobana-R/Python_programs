try:
    file1=open("tuple.txt","r")
    text=file1.read()
    print("The text inside the file are\n",text)
    
finally:
    print("In finally block")
    file1.close()
