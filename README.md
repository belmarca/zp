# zp

## Instructions

```
usage: zp.py [-h] [-f FILE] [-t TARGET]

CLI to zp bootstrap compiler.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  file to compile
  -t TARGET, --target TARGET
                        target language
```

### Example

```python
➜  zp git:(master) ✗ python3 zp.py -f examples/test/test.py -t javascript
examples/test/test.py compiled successfully to examples/test/test.js.
```
