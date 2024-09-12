from preloaded import MORSE_CODE

from itertools import groupby

MORSE_CODE = {
    '-...': 'a',
    '-.-.': 'b',
    '-..': 'c',
    '.': 'd',
    '..-.': 'e',
    '--.': 'f',
    '....': 'g',
    '..': 'h',
    '.---': 'i',
    '-.-': 'j',
    '.-..': 'k',
    '--': 'l',
    '-.': 'm',
    '---': 'n',
    '.--.': 'o',
    '--.-': 'p',
    '.-.': 'q',
    '...': 'r',
    '-': 's',
    '..-': 't',
    '.-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': ' ',
    '..--..': '?',
    '.----.': ':',
    '.-.-.-': '=',
    '.-...': '/',
    '.-.-.': '-',
    '..--': ',',
    '.-..-': "'",
    '..---': '!',
    '.-.-': '.'
}

def decode_morse(morse_code):
    morse_code = ''.join(key for key, _ in groupby(morse_code)).replace('  ', ' ')
    decoded_chars = [MORSE_CODE[m] for m in morse_code.split() if m in MORSE_CODE]
    return ' '.join(decoded_chars).strip()

print(decode_morse('.. ...-. -.--   .--- ..- -.. .'))  # HEY JUDE
