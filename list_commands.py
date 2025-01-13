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

#count()

def rajlen(input1):
    count=_0
    for i in input1:
        count +=1
        return count

    list1 = [1,2,3,4]
    print(rajlen(list1))


    #sort()

    def raj_sort(input1):
        input1.sort()
        return input1

    input1= [4,2,3,1]
    sort_list = raj_sort(input1)
    print("sorted list:",sort_list)
