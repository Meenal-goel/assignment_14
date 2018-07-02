#1- Write a Python program to read last n lines of a file

def read_last_lines(fname,n):
    with open(fname) as file:
        print("last",n,"lines of the file ",fname,"are:\n")
        data = file.readlines()
        for line in data[-n:]:
            print(line)
file_name = input("Enter the file name:")
n = int(input("Enter the number of lines to be read from last:"))
try:
    read_last_lines(file_name,n)
except Exception as e:
    print("EXCEPTION OCCURED")
    print(e)

#2.Write a Python program to count the frequency of words in a file.

def count_words(fname):
    with open(fname) as file:
        count = {}
        data = file.read()
     
        for word in data.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        for k,v in count.items():
            print(k,v)
            
            
       
file_name = input("Enter the file name:")
try:
    count_words(file_name)
except Exception as e:
    print("EXCEPTION OCCURED")
    print(e)
        
#3.Write a Python program to copy the contents of a file to another file

def copy_content(f1name,f2name):
    with open(f1name) as file:
        #note that it is necessary to open the file in write mode
        with open(f2name,"w") as f:
            for line in  file.readlines():
                f.write(line)

file_name1 = input("Enter the first file name:")
file_name2 = input("Enter the second file name:")
try:
   copy_content(file_name1,file_name2)
except Exception as e:
    print("EXCEPTION OCCURED")
    print(e)


#4. Write a Python program to combine each line from first file with the corresponding line in second file.

def combine_line(f1name,f2name):
    with open(f1name) as file:
        with open(f2name) as f:
            for line1 , line2 in zip(file,f):
                print(line1+line2)

file_name1 = input("Enter the first file name:")
file_name2 = input("Enter the second file name:")
try:
   combine_line(file_name1,file_name2)
except Exception as e:
    print("EXCEPTION OCCURED")
    print(e)

#5. Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

def key_fun(line):
    return int(line.lstrip().split(' ')[0])
def sort_num(f1name,f2name):
    sample = []
    with open(f1name) as file:
        for line in file:
            sample.append(line.strip())
      
    ans = sorted(sample,key = key_fun)
    print(ans)

    with open(f2name,"w") as f:
        for ele in sample:
            f.write(str(ele))

file_name1 = input("Enter the first file name:")
file_name2 = input("Enter the second file name:")
try:
   sort_num(file_name1,file_name2)
except Exception as e:
    print("EXCEPTION OCCURED")
    print(e)          

#another way of doing same question
import random

file = open("Random.txt", "w" )


for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 100))
    file.write(line)
    file.write("\n")
         

file.close()
f1 = open("Random.txt","r")
f2 = open("e3.txt","w")
list1 = f1.readlines()
list1.sort()
f2.writelines(list1)
f1.close()
f2.close()


                
      
