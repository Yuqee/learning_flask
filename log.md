# Learning log
## Date: Jun 3, 2023

1. `pip install flask` in **terminal** to intall *flask*
2. Create a new file named *app.py* in this directory. The content is as follows:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!<h1>'
```
3. Run this by typing `flask run` in **terminal**
4. Add placeholder in *URL*. Change the $5th$ to $7th$ line in *app.py* :
```python
@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!<h1>'.format(name)
```
```python
@app.route('/<name>')
def index(name):
    return f'<h1>Hello {name}!<h1>'
```
5. Both of them will work and the result is like the following. **Notice** that `Kaiqi` is the *value* in *variable* `name` and the last word in the *URL*
<img src="./imgs/d01p01.png" alt="img" style="zoom:33%;" />