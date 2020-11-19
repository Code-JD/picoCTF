# dont-use-client-side

## Can you break into this super secure portal?

* [https://jupiter.challenges.picoctf.org/problem/29835/](https://jupiter.challenges.picoctf.org/problem/29835/)

* [http://jupiter.challenges.picoctf.org:29835](http://jupiter.challenges.picoctf.org:29835)

* Link to website that has an input field with a button "verify", Text reads:

``` text
* This is the secure login portal
* Enter valid credentials to proceed
```

* Inspected website and found the flag jumbled in the javascript function "verify"

``` javascript
<script type="text/javascript">
  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '723c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_7') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'e}') {
```
