def validate_value( score):
    try:
        val = int(score)
    except ValueError:
        print(f"Value {score} is not an int")
        return False
    return  True