# Puzzle 8!
# Rahe hale khodam!

def sfind(a,b):
    if len(b) > len(a):
        return -1
    for i in range(len(b)):
        if a.find(b[i]) == -1:
            return -1
    return 1

def shfind(a,b):
    if len(b) != len(a):
        return -1
    for i in range(len(b)):
        if a.find(b[i]) == -1:
            return -1
    return 1

def menha(a,b):
    men = ''
    for i in range(len(a)):
        if b.find(a[i]) == -1:
            men += a[i]
    return men

f = open('data/puzzle8.txt', 'r')
data = [s.split(' | ') for s in f.read().split('\n')]

tedad = 0
sum = 0

for i in range(len(data)):
    yek = ''
    haft = ''
    char = ''
    hasht = ''

    sefr = ''
    do = ''
    se = ''
    panj = ''
    shish = ''
    noh = ''

    data[i][0] = data[i][0].split(' ')
    data[i][1] = data[i][1].split(' ')

    # part 1:
    for n in range(4):
        if len(data[i][1][n]) == 2 or len(data[i][1][n]) == 3 or len(data[i][1][n]) == 4 or len(data[i][1][n]) == 7:
            tedad += 1
    
    # part 2:
    for n in range(10):
        if len(data[i][0][n]) == 2:
            yek = data[i][0][n]
            break
    for n in range(10):
        if len(data[i][0][n]) == 3:
            haft = data[i][0][n]
            break
    for n in range(10):
        if len(data[i][0][n]) == 4:
            char = data[i][0][n]
            break
    for n in range(10):
        if len(data[i][0][n]) == 7:
            hasht = data[i][0][n]
            break
    for n in range(10):
        if data[i][0][n] == yek or data[i][0][n] == haft or data[i][0][n] == char or data[i][0][n] == hasht:
            continue
        else:
            if len(data[i][0][n]) == 5:
                if sfind(data[i][0][n], yek) == 1:
                    se = data[i][0][n]
                else:
                    if sfind(data[i][0][n], menha(char, yek)) == 1:
                        panj = data[i][0][n]
                    else:
                        do = data[i][0][n]
            else:
                if sfind(data[i][0][n], yek) != 1:
                    shish = data[i][0][n]
                else:
                    if sfind(data[i][0][n], menha(char, yek)) == 1:
                        noh = data[i][0][n]
                    else:
                        sefr = data[i][0][n]
    for n in range(4):
        if shfind(data[i][1][n], yek) == 1:
            sum += 1 * (10**(3-n))
            data[i][1][n] = 1
        elif shfind(data[i][1][n], do) == 1:
            sum += 2 * (10**(3-n))
            data[i][1][n] = 2
        elif shfind(data[i][1][n], se) == 1:
            sum += 3 * (10**(3-n))
            data[i][1][n] = 3
        elif shfind(data[i][1][n], char) == 1:
            sum += 4 * (10**(3-n))
            data[i][1][n] = 4
        elif shfind(data[i][1][n], panj) == 1:
            sum += 5 * (10**(3-n))
            data[i][1][n] = 5
        elif shfind(data[i][1][n], shish) == 1:
            sum += 6 * (10**(3-n))
            data[i][1][n] = 6
        elif shfind(data[i][1][n], haft) == 1:
            sum += 7 * (10**(3-n))
            data[i][1][n] = 7
        elif shfind(data[i][1][n], hasht) == 1:
            sum += 8 * (10**(3-n))
            data[i][1][n] = 8
        elif shfind(data[i][1][n], noh) == 1:
            sum += 9 * (10**(3-n))
            data[i][1][n] = 9
        else:
            data[i][1][n] = 0

print(tedad)
print(sum)




# with open("data/puzzle8.txt") as file:
#     input = [[part for part in line.split(" | ")] for line in file.read().strip().split("\n")]

# # part 1
# unique = sum(len(word) in [2, 3, 4, 7] for line in input for word in line[1].split(" "))
# print(unique)


# # part 2
# def get_frequencies(config):
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     return {letter: str(config.count(letter)) for letter in list(letters)}


# def get_numeric_representation(frequencies, config_word):
#     temp = [frequencies[letter] for letter in list(config_word)]
#     temp.sort()
#     return int(''.join(temp))


# def sort_letters(word):
#     word = list(word)
#     word.sort()
#     return ''.join(word)


# digits_representation = "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"  # 0 - 9
# digit_frequency = get_frequencies(digits_representation)
# digits_value = {}

# for i, digit_representation in enumerate(digits_representation.split(' ')):
#     numeric_reppresentation = get_numeric_representation(digit_frequency, digit_representation)
#     digits_value[numeric_reppresentation] = str(i)

# summation = 0
# for configuration, numbers in input:
#     config_frequencies = get_frequencies(configuration)
#     config_digits = {sort_letters(word): digits_value[get_numeric_representation(config_frequencies, word)]
#                      for word in configuration.split(' ')}

#     summation += int(''.join([config_digits[sort_letters(number)] for number in numbers.split(" ")]))
#     print(int(''.join([config_digits[sort_letters(number)] for number in numbers.split(" ")])))

# print(summation)


"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.
As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.
Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....
  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.
The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)
So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.
For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.
For example, here is what you might see in a single entry in your notes:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)
Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.
Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.
For now, focus on the easy digits. Consider this larger example:
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).
In the output values, how many times do digits 1, 4, 7, or 8 appear?
Your puzzle answer was 355.
--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:
    acedgfb: 8
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    dab: 7
    cefabd: 9
    cdfgeb: 6
    eafb: 4
    cagedb: 0
    ab: 1
Then, the four digits of the output value can be decoded:
    cdfeb: 5
    fcadb: 3
    cdfeb: 5
    cdbaf: 3
Therefore, the output value for this entry is 5353.
Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:
    fdgacbe cefdb cefbgd gcbe: 8394
    fcgedb cgb dgebacf gc: 9781
    cg cg fdcagb cbg: 1197
    efabcd cedba gadfec cb: 9361
    gecf egdcabf bgf bfgea: 4873
    gebdcfa ecba ca fadegcb: 8418
    cefg dcbef fcge gbcadfe: 4548
    ed bcgafe cdgba cbgef: 1625
    gbdfcae bgc cg cgb: 8717
    fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.
For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
Your puzzle answer was 983030.
Both parts of this puzzle are complete! They provide two gold stars: **
"""