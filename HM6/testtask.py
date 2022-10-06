expr = '1+2*3'
expr = expr.replace(' ', '')
operators = {
    '/': lambda x, y: x/y,
    '*': lambda x, y: x*y,
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y
}
for oper in operators:
    expr = expr.replace(oper, f'#{oper}#')
terms = expr.split('#')

for oper in operators:
    while True:
        try:
            i = terms.index(oper)
            result = operators.get(oper)(int(terms[i-1]), int(terms[i+1]))
            terms[i] = result
            del terms[i-1]
            del terms[i]
        except:
            break
print(terms)
