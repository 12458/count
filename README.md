# CountAPI

This API allows you to create simple numeric counters. \
You can
- create a counter
- increment a counter
- decrement a counter

All counters are accessible if the key and site values are known (i.e. are public).

## Usage

Each counter is identified inside a **namespace** with a **key**. \
The namespace should be unique, so its recommend using your site's domain. \
Inside each namespace you can generate all the counters you may need. \
\
The hit endpoint provides increment by one counters directly. \
Each time its requested the counter will increase by one: 
```sh
https://count.aws.shangen.org/api/incr/namespace/key
⇒ HTTP: 200 { "value": 1 }
```

## Examples
### Simple site visit counter
> Remember to change the items labeled in `{...}` to your desired site and key!
```html
<div id="visits">...</div>
```
```js
fetch('https://count.aws.shangen.org/api/incr/{shangen.org}/{visits}')
  .then((response) => response.json())
  .then((data) => document.getElementById('visits').innerText = data);
```

## API Documentation
API Documenation can be accessed [here](https://count.aws.shangen.org/docs)

## Licence
All code in this repository is licensed under the MIT License
```
Copyright 2022 Sim Shang En

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
