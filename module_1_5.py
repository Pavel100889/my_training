immutable_var=(100,1.123,'text1')
print(immutable_var)
mutable_list=[(immutable_var),103.5,'text2']
print(mutable_list)
mutable_list[0]=(102,103)
mutable_list[1]=104
mutable_list[2]='text3'
print(mutable_list)