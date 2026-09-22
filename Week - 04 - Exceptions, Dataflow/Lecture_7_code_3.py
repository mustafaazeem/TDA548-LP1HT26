'''
A functional (data flow driven approach) to write code. Note how we call
functions in a chain at line 44
'''
scores = [
    ["12", "15", "missing"],
    ["8", "10", "9"],
    ["18", "absent", "13"],
]

def gen_score(score_matrix):
    for raw_record in score_matrix:
        yield raw_record 


def process_record(raw_record):
    record = []
    for element in raw_record:
        try:
            record.append(int(element))

        except ValueError as e:
            record.append(0)
    
    return record

def sum_points(record):
    return sum(record)

def assign_grades(total_marks):
    if total_marks > 30:
        return 5
    elif total_marks > 25:
        return 4
    elif total_marks > 20:
        return 3
    else:
        return 'U'
    
for raw_record in gen_score(scores):
    # this line is written in a functional style that exhibits how 
    # data flows inside our system. That is a more natural match 
    # to a data flow diagram 
    print(assign_grades(sum_points(process_record(raw_record)))) 


    # Down here is more imperative style programming, which exhibits how
    # control flows inside of our system. 
    # Nonetheless, data is also present, but we make programm in a more 
    # control oriented way 

    # # print(raw_record)
    # record = (process_record(raw_record))
    # total_marks = sum_points(record) 
    # # print(total_marks)
    # grade = assign_grades(total_marks)
    # print(grade)
