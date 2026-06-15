def evaluate_sol(functions, tests):

    for i, test in enumerate(tests):
        result = functions(**test['input'])

        print(f"Test Case {i + 1}")
        print(f"Expected: {test['output']}")
        print(f"Got:      {result}")

        if result == test['output']:
            count = count + 1
            print("PASS")
        else:
            print("FAIL")

        print("-" * 20)



tests = [

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
    }
] #list of dictionaries with input and output

