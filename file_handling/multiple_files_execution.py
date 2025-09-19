
files = ["session1.txt","session2.txt"]

for f in files:
    with open(f,"w") as file:
        file.write('RGB Servers started successfully\n')
        file.write('P2P Matches started successfully\n')
        
for f in files:
    print(f'contents of {f}: ')
    with open(f,"r") as file:
        content = file.readlines()
        for line in content:
            print(line)
#            print(f'{line.strip()}\n')