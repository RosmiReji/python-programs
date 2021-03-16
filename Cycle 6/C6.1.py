file=open('geek.txt','r')
for each in file:

    print (each)


    def file_read(fname):
        with open(fname) as f:
            content_list = f.readlines()
            print(content_list)

file_read('geek.txt')

