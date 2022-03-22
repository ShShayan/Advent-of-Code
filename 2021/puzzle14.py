def charInserter(mainChar, inserti, position):
    new = mainChar[:position] + inserti + mainChar[position:]
    return new

def inserter(template, instructions):
    # aval joft harf ha ro joda mikonim
    # dovom dastore monaseb ro peyda mikonim
    # harf morede nazar ro insert mikonim
    tool = len(template)-1
    inserti = ''
    for i in range(tool):
        horof = template[i] + template[i+1]
        inserti += instructions[instructions.find(horof) + 6]
    for i in range(len(inserti)):
        template = charInserter(template, inserti[i], i * 2 + 1)
    return template

def shomarande(template):
    max = 0
    min = 10000
    for i in range(26):
        tedad = template.count(chr(65 + i))
        if tedad > max:
            max = tedad
        if tedad < min and tedad != 0:
            min = tedad
    return max, min

data = open('data/puzzle14.txt').read().split('\n\n')
template = data[0]
instructions = data[1]
for i in range(10):
    template = inserter(template, instructions)
max, min = shomarande(template)
print(f'first part answer is {max - min}')

# This obviusly only works for the first part of challenge