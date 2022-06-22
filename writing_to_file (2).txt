try:
    file1=open("writing_to_file.txt","a")
    file1.write("This information recently got appended")
    
    
    
finally:
    print("In finally block")
    file1.close()
