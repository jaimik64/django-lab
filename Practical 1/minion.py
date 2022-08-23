# def minionGameHigh(str):
#     result = {'Stuart': 0, 'Kevin': 0}
#     vowels = ['A', 'E', 'I', 'O', 'U']

#     for i in range(len(str)):
#         for j in range(i+1,len(str)+1):
#             if str[i:j][0] in vowels:
#                 result['Kevin'] = result['Kevin'] + 1
#             else:
#                 result['Stuart'] = result['Stuart'] + 1

#     if result['Kevin'] == result['Stuart']:
#         print('Game Draw')
#     elif result['Kevin'] > result['Stuart']:
#         print('Kevin ', result['Kevin'])
#     else:
#         print('Stuart ', result['Stuart'])

#NOTE: Understand Low again
 
def minionGameLow(str):
    result = {'Stuart': 0, 'Kevin': 0}
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(len(str)):
        if str[i] in vowels:
            result['Kevin'] = result['Kevin'] + len(str[i:])
        else:
            result['Stuart'] = result['Stuart'] + len(str[i:])

    if result['Kevin'] == result['Stuart']:
        print('Game Draw')
    elif result['Kevin'] > result['Stuart']:
        print('Kevin ', result['Kevin'])
    else:
        print('Stuart ', result['Stuart'])


str = input("Enter String : ").upper()

minionGameLow(str)