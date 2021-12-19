# 教育机构：广东理工；
# 作者:陈江龙；
# 地点:广东理工；
# 时间: 2021/12/12 17:18
s='li'
h=s+'fla'
print('1',h,'\n')

a1=(1,2,3,4)
print('2',a1)
a3=1,2,3,4
print('2',a3)
a4=tuple((1,2,3,4))
print('2',a4)
a2=(0,)
print('2',a2,'\n')

b1=(1,[2,3],4)
b1[1].append(1000)
print('3',b1,'\n')

c1=(1,2,3,4,5,6,7)
c2=(1,2,3,4,5,6,7)
print('4',c1[1])
print('4',c1[1:5])
for i in c1:
    print('4',i,end='\t')
print('\n')

s1={1,2,3,4,5,6,7,8,9}
s2=set([1,2,3,4,5,6,7,8,9])
print('5',s1)
s3=set(range(10))
print('5',s3,'\n')

v1={1,2,3,4,5,6,7,8,9}
print('6',9 in v1)
v1.add(90)
print('6',v1)
v1.update({'a','b'})
print('6',v1)
v1.update((65,))
print('6',v1)
v2={1,2,3,4,5,6,7,8,9,'a'}
v2.discard(2)
print('6',v2)
v2.pop()
print('6',v2)
v2.clear()
print('6',v2,'\n')

p1={1,2,3,4,5,6,7,8,9}
p2={1,2,3,4}
print('7', p2.issubset(p1))
print('7', p2.issuperset(p1))


