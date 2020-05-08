# zp

## Instructions

```python
python3 -i zp.py
compile_file('test.py', scheme)
compile_file('test.py', javascript)
```

Contents of `test.scm` (pretty-printed):

```
(define x 1)
(define y 2)
(define z 3)
(define f 0)
(define g 1)
(define q "Hello, world!")
(define r "Hello, \"world\"!")
(define s "Hello, \"world\"!")
(define t "Hello, \"world!")
(define u "Hello, \"\"\"world!")

(define function_name
  (lambda (x y z) x))

(define myfun
  (lambda (x y)
    (if (and (> x y) (< x 0))
        x)))

(define fib
  (lambda (n)
    (if (equal? n 1)
        1
        (if (equal? n 0)
            0
            (+ (fib  (- n 1)) (fib  (- n 2)))))))
```

Contents of `test.js` (pretty-printed):

```javascript
var x = 1;
var y = 2;
var z = 3;
var f = 0;
var g = 1;
var q = "Hello, world!";
var r = "Hello, \"world\"!";
var s = "Hello, \"world\"!";
var t = "Hello, \"world!";
var u = "Hello, \"\"\"world!";

function function_name(x, y, z) {
    return x;
};

function myfun(x, y) {
    if ((x > y) && (x < 0)) {
        return x;
    }
};

function fib(n) {
    if ((n === 1)) {
        return 1;
    } else {
        if ((n === 0)) {
            return 0;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }
};
```
