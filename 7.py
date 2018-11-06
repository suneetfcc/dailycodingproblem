"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

mapping = {str(k): chr(k + 96) for k in range(1,27)}
print(mapping)


def decode(message):
    no_match = []
    total = 0
    for k in mapping:
        if message.find(k) == -1:
            no_match.append(True)
        else:
            no_match.append(False)
            new_message = message.replace(k, mapping[k], 1)
            total += decode(new_message)

    if all(no_match):
        return 1
    else:
        return total


decode('111')