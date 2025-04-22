standard_operators = {
    '!=', '%', '%=', '&', '&=', '*', '**', '**=', '*=', '+', '+=', '-', '-=', '/', '//', '//=', '/=',
    '<', '<<', '<<=', '<=', '=', '==', '>', '>=', '>>', '>>=', 'False', 'If', 'None', 'True', '[]',
    '^', '^=', 'and', 'break', 'continue', 'i[-1]', 'i[0]', 'i[1]', 'in', 'is', 'is not', 'isinstance',
    'len', 'not', 'not in', 'or', 'x[:2]', 'x[2:]', '|', '|=', '~'
}


cosmicray_operators = {
    '!=', '%', '&', '*', '**', '+', '-', '/', '//', '<', '<<', '<=', '==', '>', '>=', '>>',
    'False', 'True', '[]', '^', 'and', 'break', 'continue', 'is', 'is not', 'not', 'or', '|', '~'
}


mutatest_operators = {
    '+=', '-=', '*=', '/=',
    '+', '-', '/', '*',
    '&', '|', '^',
    '<<', '>>',
    'and', 'or',
    '==', '>=', '<', '<=', '!=',
    'in', 'not in',
    'is', 'is not',
    'If',  # Representing `if` mutation
    'i[0]', 'i[1]', 'i[-1]',  # Representing index mutations
    'True', 'False', 'None',  # Representing NameConstant mutations
    'x[:2]', 'x[2:]'  # Representing slice mutations
}

mutmut_operators = {
    '+', '-', '*', '/', '//', '%', '**', '<<', '>>', '&', '|', '^', '~',
    '+=', '-=', '*=', '/=', '//=', '%=', '<<=', '>>=', '&=', '|=', '^=', '**=', '~=',
    '<', '<=', '>', '>=', '==', '!=', '<>'
}

mutpy_operators = {
    '+', '-', '*', '/', '//', '%', '**', 
    '&', '|', '^', '<<', '>>', 
    '=', '+=', 
    '<', '<=', '>', '>=', '==', '!=', 
    'and', 'or', 'not', 
    '[]', '.', 'in',
    'instance', 'len'
}


# Calculate the fault model coverage
cosmicray_coverage_percentage = round((len(cosmicray_operators.intersection(standard_operators)) / len(standard_operators)) * 100, 2) 
mutatest_coverage_percentage = round((len(mutatest_operators.intersection(standard_operators)) / len(standard_operators)) * 100, 2)
mutmut_coverage_percentage = round((len(mutmut_operators.intersection(standard_operators)) / len(standard_operators)) * 100, 2)
mutpy_coverage_percentage = round((len(mutpy_operators.intersection(standard_operators)) / len(standard_operators)) * 100, 2)
print('Cosmic-ray :',cosmicray_coverage_percentage,'%')
print('Mutatest :',mutatest_coverage_percentage,'%')
print('Mutpy :',mutpy_coverage_percentage,'%')
print('MutMut:',mutmut_coverage_percentage,'%')
