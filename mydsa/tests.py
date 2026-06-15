def evaluate_sol(functions, tests):
    count = 0
    lengthOfTests = len(tests)

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

    if count == lengthOfTests:
        print("All test cases passed!")
        print("-" * 22)
    else:
        print(f"{count} out of {lengthOfTests} test cases passed.")
        print("-" * 30)

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}


tests = [] #list of dictionaries with input and output

#query occurs in the middle

tests.append(test) 

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

#query is the first element

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 13
    },
    'output': 0
})

#query is the last element

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 0
    },
    'output': 7
})

#card does not contain query

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 2
    },
    'output': -1 #assuming we return -1 if the query is not found
})

# duplicate elements in cards

tests.append({
    'input': {
        'cards': [13, 11, 10, 10, 10, 7, 4, 4, 4, 4, 3, 1, 0],
        'query': 7
    },
    'output': 5
}) 

#query occurs multiple times in cards -> we return the index of the first occurrence of the query in cards  

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 7, 7, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})
