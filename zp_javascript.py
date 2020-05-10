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

        # byte_at -> noop
        if node.name == 'byte_at':
            return ''

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
        nargs = len(node.args)
        keywords = node.keywords

        if keywords != []:
            raise Exception

        if func == 'ord':
            return args + '.charCodeAt(0)'
        if func == 'byte_at':
            return node.args[0].id + '[' + node.args[1].id + ']'
        if func == 'range':
            # we will use
            # [...Array(5).keys()];
            # to allow using x = range(10), for example.
            # args: start, stop, step
            if nargs == 1:
                return '[...Array(' + str(node.args[0].n) + ').keys()]'
            # TODO: handle other cases!
        if func[-14:] == 'indents.append':
            return func[:-7] + '.push(' + args + ')'
        if func == 'len':
            return args + '.length'

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

            if isinstance(y, Call):
                if y.func.id == 'bytearray':
                    px = self.parse_node(x)
                    out = ' var ' + px + ' = ' + \
                        'new Uint8Array(' + str(y.args[0].n) + ')'
                    return out


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

    def parse_For(self, node):
        # We don't implement for/else.

        #TODO: do multiple args (tuples)

        # for i in range(10):
        #     body
        # for node.target.id in node.iter (Call):
        #     node.body (array)
        target = self.parse_node(node.target)
        _iter = self.parse_node(node.iter)  # handle 'range' in parse_Call
        body = '; '.join([self.parse_node(node) for node in node.body])

        out = ' for (const ' + target + ' in ' + _iter + ') {' + body + '}'
        return out

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
