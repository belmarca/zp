 (define x 1) (define y 2) (define z 3) (define f 0)  (define g 1) (define q "Hello, world!") (define r "Hello, \"world\"!") (define s "Hello, \"world\"!") (define t "Hello, \"world!") (define u "Hello, \"\"\"world!") (define function_name (lambda (x y z) x)) (define myfun (lambda (x y)  (if (and (> x y) (< x 0)) x ))) (define fib (lambda (n)  (if (equal? n 1) 1  (if (equal? n 0) 0  (+ (fib  (- n 1)) (fib  (- n 2))))))) (define comp_Num (lambda (cte ast)  (define val (ast-x ast))  (define code (lambda (rte cont) (step_end rte cont ast val))) code)) (vector-set! x i 2)(vector-ref p k)(u8vector-ref r s)