def evaluate_binary_search(functions, test):
    count = 0
    lengthOfTests = len(tests1)

    for i, t in enumerate(tests1): 
        result = functions(**t['input'])

        print(f"Test Case {i + 1}")
        print(f"Expected: {t['output']}")
        print(f"Got:      {result}")

        if result == t['output']:
            count += 1
            print("PASS")
        else:
            print("FAIL")

        print("-" * 20)

    if count == lengthOfTests:
        print("All test cases passed!")
    else:
        print(f"{count} out of {lengthOfTests} test cases passed.")


tests1 = [

     {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
    },
    {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
    },
    {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 13
    },
    'output': 0
    },
    {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 0
    },
    'output': 7
    },
    {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 2
    },
    'output': -1 #assuming we return -1 if the query is not found
    },
    {
    'input': {
        'cards': [13, 11, 10, 10, 10, 7, 4, 4, 4, 4, 3, 1, 0],
        'query': 7
    },
    'output': 5
    },
    {
    'input': {
        'cards': [13, 11, 10, 7, 7, 7, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
    },
    {
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
    }
    

] #list of dictionaries with input and output

