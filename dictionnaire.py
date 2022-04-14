dictionnaire={"salut":"hello","camion":"truck","voiture":"car","ordinateur":"computer","livre":"book"}
d={}
def add_word(mot1,mot2,d):
    for i in d.keys():
        if i==mot1 :
            if d[mot1]!=mot2:
                d[mot1]=mot2
            return d
    d[mot1]=mot2

#Tests add_word() ------------
add_word("salut","truck",d)
print(d)
add_word("salut","hello",d)
add_word("camion","truck",d)
add_word("ordinateur","computer",d)
print(d)
#-----------------------------

def display_values(d):
    res="Values using .keys() : "
    for i in d.keys():
        res+=str(d[i])+" "
    print(res)

    res2="Values using .values() : "
    for i in d.values():
        res2+=str(i)+" "
    print(res2)

#Tests display_values() ------------
display_values(d)
#-----------------------------

def delete_input(c,d):
    for i in d.keys():
        count=0
        for j in range(len(c)):
            if c[j]==i[j]:
                count+=1
            if count==len(c):
                del()

    print(res)