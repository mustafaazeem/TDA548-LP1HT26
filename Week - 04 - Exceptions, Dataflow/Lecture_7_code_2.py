'''
A generator to yield one matrix row each time next() is called
Also, we learn how to handle errors with try-except blocks 
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
            # print(f"Invalid Entry '{element}', replacing with 0")
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
    # print(raw_record)
    record = (process_record(raw_record))
    total_marks = sum_points(record) 
    # print(total_marks)
    grade = assign_grades(total_marks)
    print(grade)
