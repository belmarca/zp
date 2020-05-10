def byte_at(x, i):
    # returns an integer between 0 and 255
    if type(x) is str:
        return ord(x[i])
    else:
        return x[i]

x[i] = 2
p[k]
byte_at(r, s)

def make_char_kind():
    char_kind = bytearray(256)
    for i in range(10):
        print(i)
    return char_kind

def make_char_kind():
    char_kind = bytearray(256)
    def set_char_kind(code, tok):
        char_kind[code] = tok
    for i in range(256):
        set_char_kind(i, KIND_ERROR)
    for i in range(10):
        set_char_kind(ord('0')+i, i) # 0 .. 9
    for i in range(26):
        set_char_kind(ord('a')+i, KIND_NAME) # a .. z
        set_char_kind(ord('A')+i, KIND_NAME) # A .. Z
        set_char_kind(ord('_'), KIND_NAME)
        set_char_kind(ord('"'), KIND_STRING)
        set_char_kind(ord("'"), KIND_STRING)
        set_char_kind(ord('.'), KIND_DOT)
        set_char_kind(ord('#'), KIND_COMMENT)
        set_char_kind(ord('\\'),KIND_CONTINUATION)
        set_char_kind(ord(' '), KIND_WHITESPACE)
        set_char_kind(ord('\t'),KIND_WHITESPACE)
        set_char_kind(ord('\f'),KIND_WHITESPACE)
        set_char_kind(ord('\n'),KIND_NEWLINE)
        set_char_kind(ord('\r'),KIND_NEWLINE)
        set_char_kind(ord('*'), KIND_STAR)
        set_char_kind(ord('/'), KIND_SLASH)
        set_char_kind(ord('>'), KIND_GREATER)
        set_char_kind(ord('<'), KIND_LESS)
        set_char_kind(ord('%'), KIND_PERCENT)
        set_char_kind(ord('&'), KIND_AMPER)
        set_char_kind(ord('|'), KIND_VBAR)
        set_char_kind(ord('^'), KIND_CIRCUMFLEX)
        set_char_kind(ord('='), KIND_EQUAL)
        set_char_kind(ord('+'), KIND_PLUS)
        set_char_kind(ord('-'), KIND_MINUS) # Python3 should check -> token
        set_char_kind(ord('!'), KIND_NOT) # needs special check to reject lone !
        set_char_kind(ord('@'), KIND_AT) # Python2 doesn't have @=
        set_char_kind(ord('~'), KIND_TILDE)
        set_char_kind(ord(','), KIND_COMMA)
        set_char_kind(ord(':'), KIND_COLON)
        #set_char_kind(ord('`'), KIND_BACKQUOTE) # Python3 doesn't have `
        set_char_kind(ord(';'), KIND_SEMI)
        set_char_kind(ord('('), KIND_LPAR)
        set_char_kind(ord('['), KIND_LSQB)
        set_char_kind(ord('{'), KIND_LBRACE)
        set_char_kind(ord(')'), KIND_RPAR)
        set_char_kind(ord(']'), KIND_RSQB)
        set_char_kind(ord('}'), KIND_RBRACE)
    return char_kind

char_kind = make_char_kind()

# # The tokenizer state contains an array of bytes (the buf field) which
# # is the UTF-8 encoded source code.  An end-of-line character is added
# # to the end as a sentinel.  This avoids having to frequently test for
# # the end of input throughout the tokenizer.
# #
# # The tokenizer state contains the integer code of the most recently
# # read token (the token field) and the start and end index of that token
# # (the start and end fields).
# #
# # The tokenizer also maintains an "indents" stack to verify the validity
# # of the source code indentation, and to generate implicit
# # INDENT and DEDENT tokens corresponding to the indentation.
class TokenizerState:
    def __init__(self, buf):
        self.buf = buf + (b'\n' if isinstance(buf, bytes) else '\n')  # add sentinel
        self.buf_len = len(buf)
        self.start = 0
        self.end = 0
        self.token = token.NEWLINE
        self.line_start = 0
        self.line_num = 0
        self.paren_level = 0
        self.indents = [0]
        self.dedents = 0
        self.python = 2

ts.indents.append(col)
n = len(ts.indents)-1
ts.indents = ts.indents[:i]
# TODO:
# ts.token = token.kw.get(buf[ts.start:pos], token.NAME)
