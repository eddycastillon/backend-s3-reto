def validate_value( score):
    try:
        val = int(score)
    except ValueError:
        print(f"Value {score} is not an int")
        return False
    return  True


scores = []
for score in range(1,6,1):
    score = input(f"Ingrese nota {score}:\n")

    if validate_value(score) is True:
        scores.append(int(score))
    else:
        pass
    
    
average_scrores = sum(scores)/len(scores)

print(f"Average of score list: {average_scrores}")
print(f"Score list content: {scores}")
print(f"Max value in score list: {max(scores)}")
print(f"Min valune in score list: {min(scores)}")
