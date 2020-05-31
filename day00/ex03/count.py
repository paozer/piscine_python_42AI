import string


def text_analyzer(*args):
    """Count and display upper/lowercase, punctuation and whitespace counts."""
    if len(args) > 1:
        print("ERROR")
        return
    elif len(args) == 0:
        text = input("What is the text to analyse ?\n")
    else:
        text = args[0]
    uppercase = ''.join(c for c in text if c in string.ascii_uppercase)
    lowercase = ''.join(c for c in text if c in string.ascii_lowercase)
    punctuation = ''.join(c for c in text if c in string.punctuation)
    whitespace = ''.join(c for c in text if c in string.whitespace)
    print('The text contains {} characters:\n'.format(len(text)))
    print('- {} upper letters\n'.format(len(uppercase)))
    print('- {} lower letters\n'.format(len(lowercase)))
    print('- {} punctuation marks\n'.format(len(punctuation)))
    print('- {} spaces'.format(len(whitespace)))
