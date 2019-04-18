# 4232535363019163735331
keypad = [' =?', '.,!', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def encode(keypad, plaintext):
    coded = []
    hi = ""
    for i in plaintext:
        for x in range(len(keypad)):
            if i in keypad[x]:
                key = keypad[x]
                coded.append(str(x) + str(key.find(i)+1))
    hi = hi.join(coded)
    return hi

def decode(keypad, encoded):
    if len(encoded) % 2 != 0:
        return False
    current = ""
    s = []
    for i in encoded:
        current += i
        if len(current) == 2:
            s.append(current)
            current = ''
    c2 = ''
    for x in s:
        key = keypad[int(x[0])]
        c2 += key[int(x[1])-1]
    return c2


def main():
    print('* Nokia Cipher (Decode and Encode) *')
    while True:
        de = input('Encode or Decode (E/D)? ')
        de = de.lower()
        if de != 'e' and de != 'd':
            print('Invalid input; enter E or D')
            continue
        else:
            while True:
                if de == 'e':
                    joined = ""
                    joined = joined.join(keypad)
                    e = input('Text to encode: ').lower()
                    india = False
                    for i in e:
                        if i not in joined:
                            india = True
                            break
                    if india:
                        print(f"Error; Only input valid characters ({joined})")
                        continue
                    print(encode(keypad, e))
                elif de == 'd':
                    nums = '1234567890'
                    d = input('Text to decode: ')
                    africa = False
                    for i in d:
                        if i not in nums:
                            africa = True
                            break
                    if africa:
                        print(f"Error; Only input valid characters 0123456789")
                        continue
                    print(decode(keypad, d))
                back = input('Go back to select prompt? (Y/N) ').lower()
                if back == 'y':
                    break
                elif back == 'n':
                    continue
                else:
                    print('Invalid input; enter Y or N')

if __name__ == '__main__':
    main()


