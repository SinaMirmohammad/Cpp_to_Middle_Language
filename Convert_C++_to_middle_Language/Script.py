#Compiler
#Coding By SinaMirmohammad

#Library
import re
import os
import sys
from termcolor import colored, cprint

Banner = '''
          _             _            _   _         _        _          _             _            _       
        /\ \           /\ \         /\_\/\_\ _    /\ \     /\ \       _\ \          /\ \         /\ \     
       /  \ \         /  \ \       / / / / //\_\ /  \ \    \ \ \     /\__ \        /  \ \       /  \ \    
      / /\ \ \       / /\ \ \     /\ \/ \ \/ / // /\ \ \   /\ \_\   / /_ \_\      / /\ \ \     / /\ \ \   
     / / /\ \ \     / / /\ \ \   /  \____\__/ // / /\ \_\ / /\/_/  / / /\/_/     / / /\ \_\   / / /\ \_\  
    / / /  \ \_\   / / /  \ \_\ / /\/________// / /_/ / // / /    / / /         / /_/_ \/_/  / / /_/ / /  
   / / /    \/_/  / / /   / / // / /\/_// / // / /__\/ // / /    / / /         / /____/\    / / /__\/ /   
  / / /          / / /   / / // / /    / / // / /_____// / /    / / / ____    / /\____\/   / / /_____/    
 / / /________  / / /___/ / // / /    / / // / /   ___/ / /__  / /_/_/ ___/\ / / /______  / / /\ \ \      
/ / /_________\/ / /____\/ / \/_/    / / // / /   /\__\/_/___\/_______/\__\// / /_______\/ / /  \ \ \     
\/____________/\/_________/          \/_/ \/_/    \/_________/\_______\/    \/__________/\/_/    \_\/ 
                                                                
                         (///Dev by SinaMirmohammad / Step_1 / ///)
'''
print(colored(Banner, 'green'))

#Open_Source
File_Source = open("Source_Code_c++.cpp", "r")
Output_File = open("Output_Middle_language.txt", "a")

#Set-Null-output
Output_File.truncate(0)
#=======================
#Count Source C++ Line
Counter_source_line = 0
f0 = open("Source_Code_c++.cpp", "r")
Content_0 = f0.read() 
CoList_0 = Content_0.split("\n")
  
for i in CoList_0: 
    if i: 
        Counter_source_line += 1
f0.close
A = ("Number of source lines ==> ", Counter_source_line)
#print(colored(A, 'blue'))
#=======================

next_line = 0
for next_line in range(0, Counter_source_line + 1):

    source_line = File_Source.readline().strip()

    #"int a = 12 + 3;"
    #"int a = 12 + 13; float a = 12.3;"
    #"float a = 12.3; int a = 12 + 13;"

    print(">>> ", source_line)

    #change MultiSpace to SingleSpace
    source_line = " ".join(source_line.split())

    #print(source_line)
    index_line = source_line.split()
    #print(index_line)
    count_index_line = len(index_line)
    #print("index line ==> ",count_index_line)

    next_index_line = 0
    word_plus_word = 0

    for next_index_line in range(0,count_index_line):
        word_index_line = index_line[next_index_line]
        #print(word_index_line)
        
        #Scannes-Different-Types
        if word_index_line == "float" or "double" or "int" or "char":
            #float-variable-scanner
            if word_index_line == "float":
                Variables_plus_word_name = word_index_line + " " + index_line[next_index_line + 1]
                source_line = source_line.replace(Variables_plus_word_name,'float ID')
                float_number_index_list = re.findall("[+-]?\d+\.\d+", source_line)
                len_float_index_list = len(float_number_index_list)
                next_float_index_list = 0
                for next_float_index_list in range(0, len_float_index_list):
                    source_line = source_line.replace(float_number_index_list[next_float_index_list], 'NUM')
                    #print(source_line)
                    next_float_index_list += 1
                #print("float>>>  ",source_line)
                #print(source_line)

            #int-variable-scanner
            elif word_index_line == "int":
                Variables_plus_word_name = word_index_line + " " + index_line[next_index_line + 1]
                source_line = source_line.replace(Variables_plus_word_name,'int ID')
                '''
                digit_index_list = re.findall(r'\d+', source_line)
                len_digit_index_list = len(digit_index_list)
                next_digit_index_list = 0
                for next_digit_index_list in range(0, len_digit_index_list):
                    source_line = source_line.replace(digit_index_list[next_digit_index_list], 'num')
                    #print(source_line)
                    next_digit_index_list += 1
                print("int>>>  ",source_line)
                '''
                #print("int>>>  ",source_line)
                #print(source_line)

            #double-scanner
            elif word_index_line == "double":
                Variables_plus_word_name = word_index_line + " " + index_line[next_index_line + 1]
                source_line = source_line.replace(Variables_plus_word_name,'double ID')
                #print("double>>>  ",source_line)
                #print(source_line)

            #char scanner
            elif word_index_line == "char":
                Variables_plus_word_name = word_index_line + " " + index_line[next_index_line + 1]
                source_line = source_line.replace(Variables_plus_word_name,'char ID')
                #print("char>>>  ",source_line)
                #print(source_line)

            #Scan-Assignment-Operators
            else: #word_index_line == "=" or "+" or "+=" or "-=" or "*=" or "/=" or "%=" or "<<=" or ">>=" or "&=" or "^=" or "|=":
                if word_index_line == "=":
                    source_line = source_line.replace(word_index_line,"sim_ass_opr")

                elif word_index_line == "+=":
                    source_line = source_line.replace(word_index_line,"Add_AND_assignment_operator")

                elif word_index_line == "-=":
                    source_line = source_line.replace(word_index_line,"Subtract_AND_assignment_operator,")

                elif word_index_line == "*=":
                    source_line = source_line.replace(word_index_line,"Multiply_AND_assignment_operator")

                elif word_index_line == "/=":
                    source_line = source_line.replace(word_index_line,"Divide_AND_assignment_operator")

                elif word_index_line == "%=":
                    source_line = source_line.replace(word_index_line,"Modulus_AND_assignment_operator")

                elif word_index_line == "<<=":
                    source_line = source_line.replace(word_index_line,"Left_shift_AND_assignment_operator")

                elif word_index_line == ">>=":
                    source_line = source_line.replace(word_index_line,"Right_shift_AND_assignment_operator")

                elif word_index_line == "&=":
                    source_line = source_line.replace(word_index_line,"Bitwise_AND_assignment_operator")

                elif word_index_line == "^=":
                    source_line = source_line.replace(word_index_line,"Bitwise_exclusive_OR and_assignment_operator")
                    
                elif word_index_line == "|=":
                    source_line = source_line.replace(word_index_line,"Bitwise_inclusive_OR_and_assignment_operator")
                
                #Scan-Arithmetic Operators            
                elif word_index_line == "+":
                    source_line = source_line.replace(word_index_line,"Adds")

                elif word_index_line == "-":
                    source_line = source_line.replace(word_index_line,"Subtracts")

                elif word_index_line == "*":
                    source_line = source_line.replace(word_index_line,"Multiplies")

                elif word_index_line == "/":
                    source_line = source_line.replace(word_index_line,"Divides")

                elif word_index_line == "%":
                    source_line = source_line.replace(word_index_line,"Modulus")

                elif word_index_line == "++":
                    source_line = source_line.replace(word_index_line,"Increment")

                elif word_index_line == "--":
                    source_line = source_line.replace(word_index_line,"Decrement")
                
                #Scan-Relational-Operators
                elif word_index_line == "==":
                    source_line = source_line.replace(word_index_line,"Checks")# if the values of two operands are equal or not, if yes then condition becomes true")

                elif word_index_line == "!=":
                    source_line = source_line.replace(word_index_line,"Checks")#if the values of two operands are equal or not, if values are not equal then condition becomes true")

                elif word_index_line == ">":
                    source_line = source_line.replace(word_index_line,"Checks")# if the value of left operand is greater than the value of right operand, if yes then condition becomes true")

                elif word_index_line == "<":
                    source_line = source_line.replace(word_index_line,"Checks")# if the value of left operand is less than the value of right operand, if yes then condition becomes true")

                elif word_index_line == ">=":
                    source_line = source_line.replace(word_index_line,"	Checks")# if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true")

                elif word_index_line == "<=":
                    source_line = source_line.replace(word_index_line,"	Checks")# if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true")

                #Logical Operators
                elif word_index_line == "&&":
                    source_line = source_line.replace(word_index_line,"Called_Logical_AND operator")#. If both the operands are non-zero, then condition becomes true")
                elif word_index_line == "||":
                    source_line = source_line.replace(word_index_line,"Called_Logical_OR_Operator")#. If any of the two operands is non-zero, then condition becomes true")
                elif word_index_line == "!":
                    source_line = source_line.replace(word_index_line,"	Called_Logical_NOT_Operator")# Use to reverses the logical state of its operand. If a condition is true, then Logical NOT operator will make false")

                #print(source_line)

        #del word_index_line
        next_index_line += 1

    #Scanner-Intger-number
    digit_index_list = re.findall(r'\d+', source_line)
    len_digit_index_list = len(digit_index_list)
    next_digit_index_list = 0
    for next_digit_index_list in range(0, len_digit_index_list):
        source_line = source_line.replace(digit_index_list[next_digit_index_list], 'NUM')
        next_digit_index_list += 1
        #print(source_line)

    #Write in output file
    Output_File.write(source_line + "\n")
    print(colored('>>> ', 'red'),source_line)
    #print(">>> ",source_line)

#close_file
Output_File.close()