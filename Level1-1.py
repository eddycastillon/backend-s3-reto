scores = []
for score in range(1,6,1):
    score = input(f"Ingrese nota {score}:\n")
    scores.append(int(score))

average_scrores = sum(scores)/len(scores)

print(f"Average of score list: {average_scrores}")
print(f"Score list content: {scores}")
print(f"Max value in score list: {max(scores)}")
print(f"Min valune in score list: {min(scores)}")
