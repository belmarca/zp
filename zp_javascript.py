from common import *

class JavaScript():

    name = 'JavaScript'

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
        args = ','.join([self.parse_arg(arg) for arg in node.args])
        kwarg = ''
        return (args, kwarg)

    def parse_FunctionDef(self, node):
        args, kwarg = self.parse_arguments(node.args)
        body = '; '.join([self.parse_node(node) for node in node.body])
        name = node.name
        out = " function " + name + '(' + args + ') {'
        out += ' ' + body
        out += "};"
        return out

    def parse_Compare(self, node):
        def compare(op, l, r):
            if isinstance(op, Is):
                out = self.parse_node(op) + self.parse_node(l) + ', ' + self.parse_node(r) + ')'
            else:
                out = ' (' + self.parse_node(l) + ' ' + self.parse_node(op) + ' ' + self.parse_node(r) + ')'
            return out

        def type_compare(op, arg, typ):
            if typ == 'str':
                typ = 'string'
            elif typ == 'int':
                typ = 'number'
            elif typ == 'float':
                typ = 'number'
            elif typ == 'bool':
                typ = 'boolean'

            if isinstance(op, Is):
                out = self.parse_node(op) + '(typeof ' + arg + ')'
                out += ', ' + typ + ')'
            else:
                out = ' ((typeof ' + arg + ') ' + self.parse_node(op)
                out += ' ' + typ + ')'
            return out

        left = node.left
        ops = node.ops
        comparators = node.comparators
        # there can be more than one comparator, in which case we 'and'
        if len(ops) > 1:
            if isinstance(left, Call) and \
               left.func.id == 'type':
                out = ' && '.join([type_compare(ops[i], comparators[i].id, left.args[i].id)
                                   for i in range(len(ops))])
                return out

            out = ' && '.join([compare(ops[i], left, comparators[i])
                               for i in range(len(ops))])
        else:
            if isinstance(left, Call):
                if left.func.id == 'type':
                    return type_compare(ops[0], comparators[0].id, left.args[0].id)
            out = compare(ops[0], left, comparators[0])
        return out

    def parse_Call(self, node):
        func = self.parse_node(node.func)
        args = ','.join([self.parse_node(arg) for arg in node.args])
        keywords = node.keywords

        if keywords != []:
            raise Exception

        if func == 'ord':
            return args + '.charCodeAt(0)'

        return func + '(' + args + ')'

    def parse_BinOp(self, node):
        def binop(op, l, r):
            return self.parse_node(l) + ' ' + self.parse_node(op) + ' ' + self.parse_node(r)
        left = node.left
        op = node.op
        right = node.right
        return ' ' + binop(op, left, right)

    def parse_If(self, node):
        test = self.parse_node(node.test)  # Compare, BoolOp
        body = '; '.join([self.parse_node(node) for node in node.body])
        orelse = node.orelse
        out = " if(" + test + ') {' + body
        if orelse != []:
            out += "} else {"
            out += '; '.join([self.parse_node(node) for node in orelse]) + '}'
        else:
            out += '}'
        return out

    def parse_Assign(self, node):
        # value and targets can be tuples!
        targets = node.targets
        value = node.value

        if len(targets) > 1:
            raise Exception

        def define(x, y):
            py = self.parse_node(y)

            if isinstance(x, Subscript):
                arr = self.parse_node(x.value)
                pos = self.parse_node(x.slice)
                return arr + '[' + pos + '] = ' + py + ';'

            px = self.parse_node(x)
            return ' var ' + px + " = " + py + ';'

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
        return value + '.' + attr

    def parse_Subscript(self, node):
        value = self.parse_node(node.value)
        _slice = self.parse_node(node.slice)

        return value + '[' + _slice + ']'

    def parse_Return(self, node):
        return 'return ' + self.parse_node(node.value) + ';'

    def parse_Expr(self, node):
        return self.parse_node(node.value) + ';'

    @staticmethod
    def parse_arg(node):
        arg = node.arg
        return arg

    @staticmethod
    def parse_Add(node):
        return '+'

    @staticmethod
    def parse_Sub(node):
        return '-'

    @staticmethod
    def parse_Gt(node):
        return ">"

    @staticmethod
    def parse_GtE(node):
        return ">="

    @staticmethod
    def parse_Lt(node):
        return "<"

    @staticmethod
    def parse_LtE(node):
        return ">="

    @staticmethod
    def parse_Eq(node):
        return "==="

    @staticmethod
    def parse_NotEq(node):
        return "!=="

    @staticmethod
    def parse_Is(node):
        return "Object.is("
