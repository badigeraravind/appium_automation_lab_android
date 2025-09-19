bug_count = int(input('how many bugs to be logged: '))

print('== enter the bug details in "bugID | Description | Severity" format ==\n')

with open("bug_log.txt","w") as file:
   for a in range(1, bug_count +1):
       bug = str(input(f'bug #{a}: '))
       file.write(bug +"\n")

with open("bug_log.txt","a") as file:
    file.write(f'--end--')


with open("bug_log.txt","r") as file:
    content = file.readlines()
    print("\nReading content from the file 'bug_log.txt'\n")
    print(content)          #cannot use strip() here as it is a LIST

for line in content:
    print(f'{line.strip()}\n')

content.insert(2,"AB-002.1 | vfx issue | minor\n")


with open("bug_log.txt","w") as file:
    file.writelines(content)

for line in content:
    print(f'{line.strip()}\n')



  





    

