# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142


def ptransfer(inputs, number):
    translate = {'.':0, 'x':1}
    back = {0:'.', 1:'x'}
    power = translate[inputs[0]]*4 + translate[inputs[1]]*2 + translate[inputs[2]]*1
    binary = breakdown(number)
    return back[binary[power]]


def breakdown(number):
    binary = [0 for i in range(8)]
    i=7
    while number!=0:
        binary[i] = number%2
        number = number/2
        i=i-1
    return binary[::-1]


def cellular(strings, pattern):
    length = len(strings)
    result = ""
    for i in range(length):
        s = strings[(i - 1) % length] + strings[i] + strings[(i + 1) % length]
        result = result + ptransfer(s, pattern)

    return result


def cellular_automaton(strings, pattern, gen):

    result = cellular(strings, pattern)
    for i in range(gen-1):
        result = cellular(result, pattern)

    return result

print cellular_automaton('.x.x.x.x.', 17, 2)