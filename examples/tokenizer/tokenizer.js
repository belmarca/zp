x[i] = 2;
p[k];
r[s];

function make_char_kind() {
    var char_kind = new Uint8Array(256);
    for (const i in [...Array(10).keys()]) {
        print(i);
    };
    return char_kind;
};

function make_char_kind() {
    var char_kind = new Uint8Array(256);

    function set_char_kind(code, tok) {
        char_kind[code] = tok;
    };
    for (const i in [...Array(256).keys()]) {
        set_char_kind(i, KIND_ERROR);
    };
    for (const i in [...Array(10).keys()]) {
        set_char_kind("0".charCodeAt(0) + i, i);
    };
    for (const i in [...Array(26).keys()]) {
        set_char_kind("a".charCodeAt(0) + i, KIND_NAME);
        set_char_kind("A".charCodeAt(0) + i, KIND_NAME);
        set_char_kind("_".charCodeAt(0), KIND_NAME);
        set_char_kind("\"".charCodeAt(0), KIND_STRING);
        set_char_kind("'".charCodeAt(0), KIND_STRING);
        set_char_kind(".".charCodeAt(0), KIND_DOT);
        set_char_kind("#".charCodeAt(0), KIND_COMMENT);
        set_char_kind("\\".charCodeAt(0), KIND_CONTINUATION);
        set_char_kind(" ".charCodeAt(0), KIND_WHITESPACE);
        set_char_kind("\t".charCodeAt(0), KIND_WHITESPACE);
        set_char_kind("\x0c".charCodeAt(0), KIND_WHITESPACE);
        set_char_kind("\n".charCodeAt(0), KIND_NEWLINE);
        set_char_kind("\r".charCodeAt(0), KIND_NEWLINE);
        set_char_kind("*".charCodeAt(0), KIND_STAR);
        set_char_kind("/".charCodeAt(0), KIND_SLASH);
        set_char_kind(">".charCodeAt(0), KIND_GREATER);
        set_char_kind("<".charCodeAt(0), KIND_LESS);
        set_char_kind("%".charCodeAt(0), KIND_PERCENT);
        set_char_kind("&".charCodeAt(0), KIND_AMPER);
        set_char_kind("|".charCodeAt(0), KIND_VBAR);
        set_char_kind("^".charCodeAt(0), KIND_CIRCUMFLEX);
        set_char_kind("=".charCodeAt(0), KIND_EQUAL);
        set_char_kind("+".charCodeAt(0), KIND_PLUS);
        set_char_kind("-".charCodeAt(0), KIND_MINUS);
        set_char_kind("!".charCodeAt(0), KIND_NOT);
        set_char_kind("@".charCodeAt(0), KIND_AT);
        set_char_kind("~".charCodeAt(0), KIND_TILDE);
        set_char_kind(",".charCodeAt(0), KIND_COMMA);
        set_char_kind(":".charCodeAt(0), KIND_COLON);
        set_char_kind(";".charCodeAt(0), KIND_SEMI);
        set_char_kind("(".charCodeAt(0), KIND_LPAR);
        set_char_kind("[".charCodeAt(0), KIND_LSQB);
        set_char_kind("{".charCodeAt(0), KIND_LBRACE);
        set_char_kind(")".charCodeAt(0), KIND_RPAR);
        set_char_kind("]".charCodeAt(0), KIND_RSQB);
        set_char_kind("}".charCodeAt(0), KIND_RBRACE);
    };
    return char_kind;
};
var char_kind = make_char_kind();
class TokenizerState {
    constructor(buf) {
        var self = this;
        self.buf = buf + ((buf instanceof Uint8Array) ? "\n" : "\n");
        self.buf_len = buf.length;
        self.start = 0;
        self.end = 0;
        self.token = token.NEWLINE;
        self.line_start = 0;
        self.line_num = 0;
        self.paren_level = 0;
        self.indents = [0];
        self.dedents = 0;
        self.python = 2;
    };
}
ts.indents.push(col);
var n = ts.indents.length - 1;
var ts.indents = ts.indents.slice(0, i);
