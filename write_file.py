try:
    file1=open("writing_to_file.txt","w")
    file1.write("This is the new sample file created for file handling.\nIf file does not exist it creates one\n.Otherwise it is going to erase the data and add the new data passed")
    
    
    
finally:
    print("In finally block")
    file1.close()
