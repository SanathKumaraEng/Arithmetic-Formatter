problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

if len(problems) > 5 :
        print('Error: Too many problems.')

line1 = list()
line2 = list()
line3 = list()
line4 = list()

for problem in problems :
        if problem.find('+') == -1 and problem.find('-') == -1 :
            print("Error: Operator must be '+' or '-'.")
        terms = problem.split()
        #print(terms)
        offset = len(terms[0]) - len(terms[2])
        if offset > 0 :
            term = 2           
        elif offset < 0 :
            term = 0
            offset = offset * -1 

        if terms[0].isnumeric() and terms[2].isnumeric() : 
            n1 = int(terms[0])
            n2 = int(terms[2])
        #print(n1, " ",n2)
        else : 
            print('Error: Numbers must only contain digits.')

        if len(terms[0]) > 4 or len(terms[2]) > 4 :
            print('Error: Numbers cannot be more than four digits.')