from common import *

class Scheme():

    name = 'Scheme'

    def __init__(self, parse_node):
        self.parse_node = parse_node

    def py_parse(self, source):
        parse_tree = parse(source)
        body = parse_tree.body

        out = ''

        for node in body:
            out += self.parse_node(node)

        return out

    def parse_arguments(self, node):
        args = ' '.join([self.parse_arg(arg) for arg in node.args])
        kwarg = ''
        return (args, kwarg)

    def parse_FunctionDef(self, node):
        args, kwarg = self.parse_arguments(node.args)
        body = ' '.join([self.parse_node(node) for node in node.body])
        name = node.name

        # byte_at -> noop
        if node.name == 'byte_at':
            return ''

        out = " (define " + name + " (lambda ("
        out += args
        out += ")"
        out += ' ' + body
        out += "))"
        return out

    def parse_Compare(self, node):
        def compare(op, l, r):
            out = self.parse_node(op) + ' ' + self.parse_node(l) + ' ' + self.parse_node(r) + ')'
            if isinstance(op, NotEq):
                out += ')'
            return out

        def type_compare(typ, arg):
            if typ == 'str':
                pred = 'string?'
            elif typ == 'int':
                pred = 'integer?'
            elif typ == 'bool':
                pred = 'boolean?'
            elif typ == 'float':
                pred = 'flonum?'

            return '(' + pred + ' ' + arg + ')'

        left = node.left
        ops = node.ops
        comparators = node.comparators

        # there can be more than one comparator, in which case we 'and'
        if len(ops) > 1:

            # multiple type comparisons?
            if isinstance(left, Call):
                if left.func.id == 'type':
                    out = '(and ' + \
                        ' '.join([type_compare(comparators[i].id, left.args[i].id)
                                  for i in range(len(ops))]) + ')'
                    return out

            out = '(and ' + \
                ' '.join([compare(ops[i], left, comparators[i])
                        for i in range(len(ops))]) + \
                ')'
        else:
            # single type comparison?
            if isinstance(left, Call):
                if left.func.id == 'type':
                    return type_compare(comparators[0].id, left.args[0].id)

            out = compare(ops[0], left, comparators[0])
        return out

    def parse_Call(self, node):
        func = self.parse_node(node.func)
        args = ' '.join([self.parse_node(arg) for arg in node.args])
        keywords = node.keywords

        if keywords != []:
            raise Exception

        # RTS conversions, maybe put into a dict?
        if func == 'ord':
            func = 'char->integer'
        if func == 'byte_at':
            func = 'u8vector-ref'
            return '(' + func + ' ' + args + ')'

        return '(' + func + ' ' + args + ')'

    def parse_BinOp(self, node):
        def binop(op, l, r):
            return self.parse_node(op) + ' ' + self.parse_node(l) + ' ' + self.parse_node(r) + ')'
        left = node.left
        op = node.op
        right = node.right
        return ' ' + binop(op, left, right)

    def parse_If(self, node):
        test = self.parse_node(node.test)  # Compare, BoolOp
        body = ' '.join([self.parse_node(node) for node in node.body])
        orelse = node.orelse
        out = " (if " + test + ' ' + body + ' '
        if orelse != []:
            out += ' '.join([self.parse_node(node) for node in orelse]) + ')'
        else:
            out += ')'
        return out

    def parse_Assign(self, node):
        # value and targets can be tuples!
        targets = node.targets
        value = node.value

        if len(targets) > 1:
            raise Exception

        def define(x, y):
            # Assigns x = y
            py = self.parse_node(y)

            if isinstance(x, Subscript):
                vec = self.parse_node(x.value)
                pos = self.parse_node(x.slice)
                return ' (vector-set! ' + vec + ' ' + pos + ' ' + py + ')'

            px = self.parse_node(x)
            return ' (define ' + px + " " + py + ')'

        if isinstance(value, Tuple):
            target_elts = targets[0].elts
            value_elts = value.elts
            out = ' '.join([define(target_elts[i], value_elts[i]) for i in range(len(target_elts))])
        else:
            out = define(targets[0], value)
        return out

    def parse_Attribute(self, node):
        value = self.parse_node(node.value)
        attr = node.attr
        # Let's assume attributes are structs
        return '(' + value + '-' + attr + ' ' + value + ')'

    def parse_Subscript(self, node):
        value = self.parse_node(node.value)
        _slice = self.parse_node(node.slice)
        ctx = node.ctx

        # vector-ref by choice
        return '(vector-ref ' + value + ' ' + _slice + ')'

    def parse_Bytes(self, node):
        return 0

    def parse_Return(self, node):
        return self.parse_node(node.value)

    @staticmethod
    def parse_arg(node):
        arg = node.arg
        return arg

    @staticmethod
    def parse_Add(node):
        return '(+'

    @staticmethod
    def parse_Sub(node):
        return '(-'

    @staticmethod
    def parse_Gt(node):
        return "(>"

    @staticmethod
    def parse_GtE(node):
        return "(>="

    @staticmethod
    def parse_Lt(node):
        return "(<"

    @staticmethod
    def parse_LtE(node):
        return "(>="

    @staticmethod
    def parse_Eq(node):
        return "(equal?"

    @staticmethod
    def parse_NotEq(node):
        return "(not (equal?"

    @staticmethod
    def parse_Is(node):
        return "(eq?"
