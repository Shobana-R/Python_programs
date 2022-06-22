try:
    file1=open("writing_to_file.txt","w")
    file1.write("The previous data got erased.")
    
    
    
finally:
    print("In finally block")
    file1.close()
