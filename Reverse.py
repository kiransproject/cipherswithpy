#!/usr/bin/python

message = raw_input('Text to encrypt or decrypt : ')
translated = ''
i = len(message)-1
while i>=0:
    translated = translated+message[i]
    i=i-1

print (translated)
