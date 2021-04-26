scores = []

def validate_value( score):
    try:
        val = int(score)
    except ValueError:
        print(f"Value {score} is not an int")
        return False
    return  True

def request_value ( iteration):
    name = input(f"[{iteration}]Enter student name\n")
    scores.append({"name": name})
    scores[iteration]['scores']= []
    while True:
        score = input(f"[{name}]Enter score\n")
        if validate_value(score) is True:
            scores[iteration]['scores'].append(int(score))
            
        else:
            pass
        if input(f"Do yo want enter other note y/n?") == "y":
            print(scores)
        else:
            break

count_students = input(f"How many students do you want to enter?")
if validate_value (count_students):
    for i in range(int(count_students)):
        request_value(i)
        scores[i]['min'] = min(scores[i]['scores'])
        scores[i]['max'] = max(scores[i]['scores'])
        scores[i]['average'] = sum(scores[i]['scores'])/len(scores[i]['scores'])
else:
    pass

print(scores)