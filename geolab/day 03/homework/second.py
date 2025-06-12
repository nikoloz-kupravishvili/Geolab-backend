score = 10

first_question = input('ra hqvia katis shvils: ')
while first_question.lower() != 'knuti':
    print('wrond answer :(')
    first_question = input('ra hqvia katis shvils: ')
    score -= 1
    if first_question.lower() == 'knuti':
        print('good job :)')
        



second_question = input('ramdenia 33 + 77 : ')
while second_question != '110':
    print('wrond answer :(')
    second_question = input('ramdenia 33 + 77 : ')

    score -= 1
    if second_question == '110':
        print('good job :)')
        



third_question = input('ramdeni asoa inglisur anbanshi: ')
while third_question != '26':
    print('wrond answer :(')
    third_question = input('ramdeni asoa inglisur anbanshi: ')

    score -= 1
    if third_question == '26':
        print('good job :)')
        
    



fourth_question = input('ramdeni fexi aqvs qatams: ')
while fourth_question != '2'or fourth_question.lower() != 'two':
    print('wrond answer :(')
    fourth_question = input('ramdeni fexi aqvs qatams: ')

    score -= 1
    if fourth_question == '2' or fourth_question.lower() == 'two':
        print('good job :)')
        
    


fifth_question = input('Hello world?: ')
while fifth_question != 'ofc':
    print('wrond answer :(')
    fifth_question = input('Hello world?: ')

    score -= 1
    if fifth_question == 'ofc':
        print('good job :)')
        



print('score: ' +score)