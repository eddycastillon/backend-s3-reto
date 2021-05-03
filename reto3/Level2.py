scores = []

def validate_value( score):
    try:
        val = int(score)
    except ValueError:
        print(f"Value {score} is not an int")
        return False
    return  True

def request_value ( iteration):
    score = input(f"Ingrese nota: { iteration}\n")
    if validate_value(score) is True:
        scores.append(int(score))
    else:
        request_value(iteration)

name = input(f"Ingrese su nombre:")
for i in range(1,6,1):
    request_value(i)
    
average_scrores = sum(scores)/len(scores)
print(f"Student: {name}")
print(f"Score list content: {scores}")
print(f"Average of score list: {average_scrores}")
print(f"Max value in score list: {max(scores)}")
print(f"Min valune in score list: {min(scores)}")
