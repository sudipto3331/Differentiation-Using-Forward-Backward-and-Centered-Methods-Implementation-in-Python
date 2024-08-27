#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:39:35 2023

@author: sudipto3331
"""

def fnc(x):
    return (x*x);

def forward_oh(x, h, n):
    if n<=0:
        return 0
    elif n==1:
        result = (fnc(x+h)-fnc(x))/h
        return result
    else:
        result = (forward_oh(x+h, h, n-1)-forward_oh(x, h, n-1))/h
        return result

def forward_oh2(x, h):
    result = (-fnc(x+h+h)+(4*fnc(x+h))-(3*fnc(x)))/(2*h)
    return result

def backward_oh(x, h):
    result = (fnc(x)-fnc(x-h))/h
    return result

def backward_oh2(x, h):
    result = (fnc(x-h-h)-(4*fnc(x-h))+(3*fnc(x)))/(2*h)
    return result

def center_oh(x, h):
    result = (fnc(x+h)-fnc(x-h))/(2*h)
    return result

def center_oh2(x, h):
    result = (-fnc(x+h+h)+(8*fnc(x+h))-(8*fnc(x-h))+(fnc(x-h-h)))/(12*h)
    return result

order = float(input("Enter the derivative order: "));
point = float(input("Enter the differenting point: "));
h = float(input("Enter the step size: "));
method = float(input("Select Method:\n1. Forward\n2. Backward\n3.Centered\nEnter Choice:"));
accuricy = float(input("Select Accuricy:\n1. O(h)\n2. O(h^2)\nEnter Choice:"));
    

if method==1:
    if accuricy==1:
        if (forward_oh(point, h, order)) <= 0:
            print("Differention not possible")
        else:
            print("Result:", forward_oh(point, h, order))
        
    elif accuricy==2:
        print("Result:", forward_oh2(point, h))
elif method==2:
    if accuricy==1:
        print("Result:", backward_oh(point, h))
    elif accuricy==2:
        print("Result:", backward_oh2(point, h))
    
elif method==3:
    if accuricy==1:
        print("Result:", center_oh(point, h))
    elif accuricy==2:
        print("Result:", center_oh2(point, h))
