#!/usr/bin/env python
# coding: utf-8

# In[2]:


def clear():
    import os
    os.system('clear')
    
def SeperatedPairs(list_value):
    for i in range(0, len(list_value), 2):
        yield list_value[i:i + 2]

        
def LibImport(note_file):
    import PyPDF2
    Obj = open(note_file,'rb')
    reader = PyPDF2.PdfReader(Obj)
    return reader

def QuestionFinder(pdfText):
    temp_list = []
    question = ""
    question_list = []
    count = 0
    q_count = 0
    j = None
    k = None
    total_questions = 0
    length_of_list = 0
    

    for i in pdfText:  
        count = count + 1 
        if i == "*": 
            q_count = count 
           
            j = pdfText[q_count]
            
            temp_list.append(q_count)
            
            while k != "*": 
                for j in pdfText[q_count]: 
                    if j == "*":
                        k = j
                        break      
                    else:
                        question = question + j 
                        q_count = q_count + 1 
            i = pdfText[count+1] 
            
    pairs = list(SeperatedPairs(temp_list))
        
        
    length_of_pairs = len(pairs)
    
    for x in pairs:
        question = pdfText[x[0]:x[1]]
        question_list.append(question)
        question = ""
            

    return question_list


def QuestionOrganizer(list_of_questions):
    counter = 0
    index_question = 0
    question = ""
    updated_q_list = []
    dict_of_QA = {}
    index_count = 0
    
    while counter < len(list_of_questions):
        
        for i in list_of_questions[index_question]:
            if (i == "\n") and ((list_of_questions[index_question][index_count-1] == "?") or (list_of_questions[index_question][index_count-1] == ":")):
                question = question + "|"
                index_count = index_count + 1
                
                
            elif i == "\n":
                question = question + " "
                index_count = index_count + 1
            
            elif i == "●":
                question = question + "\n-"
                index_count = index_count + 1
                
            elif i == "?":
                question = question + "?\n"
                index_count = index_count + 1
            
            elif i == "*":
                question = question + ""
                index_count = index_count + 1
                
            else:
                question = question + i
                index_count = index_count + 1
                
        updated_q_list.append(question)
        question = ""
        index_question = index_question + 1
        counter = counter + 1
        index_count = 0
    
    
    counter = 0
    count = 0
    
    index_question = 0
    question = ""
    
    answer_start_pos = []
    
    
    index_answer = 0
    answer = ""
    
    
    while counter < len(updated_q_list):
        
        for y in updated_q_list[index_question]:
            if y != "|":
                question = question + y
                count = count + 1
                
            else:
                count = count+1
                answer_start_pos.append(count)
                break
                
        
        
        for z in updated_q_list[index_answer][answer_start_pos[index_answer]:]:
            if z == "*":
                answer = answer + "\n"
                break
            
            else:
                answer = answer + z
                
    

        
        dict_of_QA[question] = answer
        question = ""
        answer = ""
        count = 0
        counter = counter + 1
        
        index_question = index_question + 1
        index_answer = index_answer + 1
        
        
        

    return dict_of_QA


def FinalOutput(pdfdict):
    count = 0
    valid_input = False
    while count < len(pdfdict):

        for key in pdfdict:
            valid_input = False
            print("Question ({})".format(count+1))
            print(key)

            while valid_input != True:
                input_flip = input("\nDo you want to see the Answer? \nY/N: ")

                if input_flip.upper() == "Y":
                    print("\n")
                    print(key)
                    print(pdfdict[key])
                    valid_input = True
                    print('\n\n')
                    count = count + 1
                    clear()

                else:
                    print("\n")
                    print("Question ({})".format(count+1))
                    print(key)
                    valid_input = False
                    clear()


pdfFileInput = input("Enter your PDF Filename: ")

reader = LibImport(pdfFileInput)

length_of_pdfNotes = len(reader.pages)

page_count = 0

while page_count < length_of_pdfNotes:
    
    pageObj = reader.pages[page_count]
    
    pdfText = pageObj.extract_text()
    
    question_list = QuestionFinder(pdfText)
        
    organized_questions = QuestionOrganizer(question_list)
    
    FinalOutput(organized_questions)
    page_count = page_count + 1













# In[ ]:




