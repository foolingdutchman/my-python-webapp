#!/usr/bin/env python

print 'hello world'


height=input('input the height:')
weight= input('input the weight')
height=float(height)
weight=float(weight)
bmi = weight/(height*height)
if bmi<18.5:
    print('too thin!')
elif bmi<25:
    print('normal')
elif bmi<28:
    print('overweight')
elif bmi<32:
    print('fat')
else :
    print('seriously fat!')
