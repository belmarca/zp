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

function comp_Num(cte, ast) {
  var val = ast.x;

  function code(rte, cont) {
    return step_end(rte, cont, ast, val);
  };
  return code;
};
x[i] = 2;
p[k];
r[s];
