# Program to create a file of usernames in batch mode.

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")
    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")
    
    # open the files
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')
    
    # process each line of the input file
    for line in infile.readlines():
        # get the first and last names from line
        first, last = line.split(' ')
        # create the username
        uname = first[0].lower()+last[:7].lower()
        # write it to the output file
        outfile.write(uname+'\n')
        
    # close both files
    infile.close()
    outfile.close()
    
    print("Usernames have been written to", outfileName)

main()
