#append()
def raj_append(input1,input2):
    for i in input2:
        input1.append(i)
        return input1

list1 = [1,2,3,4]

i =[5]

new_list= raj_append(list1,i)

print(new_list)


#length()

def len_raj(input1):
    length = 0
    for i in input1:
        length +=1 
        return length
    
    list1 =[1,2,3,4]
    length_list= len_raj(list1)
    print(length_list)

