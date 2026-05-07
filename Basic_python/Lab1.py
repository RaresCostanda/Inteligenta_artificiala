word='reviver'
p=bool(word.find(word[::-1])+1)
print(p)

type(1)
type(-100)
type(0.0)
type(2.2)
type(2E4)

a1=10//3
a2=10%3
a3=10**3
print(a1,a2,a3)

a4=pow(5,2)
print(a4)
abs(-25)
print(abs(-25))
print(round(5.567))
print(round(5.468, 2))
print(bin(512))
print(hex(234))

#age=input("How old are you?")
#age=int(age)

type('Helllooooo')
name='John Doe'
print(name[2])
print(name[:])
print(name[::1])
print(name[:1])
print(name[1:])
print(name[-1])
print(name[::-1])
print(name[0:7:2])

print('Hi there' +' '+ 'John')
print('*'*100)

len('salut')
print(len('salut'))

a5='On an island'.strip('d')
print(a5)

a6='si uite asa testam tot felul de functii'.split()
print(a6)
print('Need to make fire'.startswith('Need'))
print('still there'.upper())
print('ceva ceva'.capitalize())
print('oh, hi there'.find('e'))

name1='Andrei'
name2='Sonny'
print(f'Hello there {name1} and {name2}')

myList=[1,2,'3',True]
print(myList[::-1])
print(myList[0:3:2])
print(myList*2)
print(myList +[100])
print(myList.append(100))
print(myList.extend([100,200]))
print(myList.insert(2,'!!!!'))
print([1,2,3].pop())
print([1,2,3,5,4].sort())
print(sorted([1,2,3,4,5]))
print(sorted([1,2,3,4,5],reverse=True))
print(list(reversed([1,2,3,4,5])))
mylist=[34,22,37,45,54,67,98,15]
first, *x, last = mylist
print(first)
print(last)

myDict={'name':'John Doe', 'age':'25', 'magic_power':False}
print(list(myDict.keys()))
print(list(myDict.values()))
print(list(myDict.keys()))
print(list(myDict.items()))
myDict['favourite_snack']='Grapes'
print(list(myDict.values()))
myDict.get('age')
myDict.get('ages', 0)

myTuple=['apple','grapes','mango','grapes']
print(myTuple.index('grapes'))
print(myTuple.count('grapes'))

my_set=set()
my_set.add(1)
my_set.add(100)
print(my_set)
myList1=[1,2,3,3,3,4,4,5,6,1]
set(myList1)
my_set.remove(100)
my_set.discard(100)
print(my_set)

set1={1,2,3}
set2={3,4,5}
set3=set1.symmetric_difference(set2)
print(set3)
print(set1.issuperset(set2))
print(set1.issubset(set2))
print(set1.isdisjoint(set2))









