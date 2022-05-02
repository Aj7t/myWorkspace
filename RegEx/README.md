## Notes  on regex

#### python 
MetaCharacters: <br>
[] . ^ $ * + ? {} () \ |  <br>
_________________________________________________
 <br>
^ : start   <br>
$ : end   <br>
[] : character set   <br>
[^] : negation  <br>
(|) : or operator  <br>
(\) : CHARACTER IS not threaten in any way   <br>
(*) : matches zero or more occurrences of the pattern left to it  <br>
(+) : matches one or more occurrences of the pattern left to it  <br>
(?) : matches zero or one occurrence of the pattern left to it  <br>
{n,m} : This means at least n, and at most m repetitions of the pattern left to it.  <br>

 <br> <br>
**Reference link** [click here :](https://www.programiz.com/python-programming/regex)


### Email validation 

```
'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
```

### Phone number validation

```
'\+?(0|91)?[7-9][0-9]{9}'
```
### STD number validation

```
'^(0)?[1-9](0|[1-9]){1,3}$'
```

### pin code validation

```
'^[0-9]{6}$'
```

### Pan number validation

```
'[A-Z]{5}[0-9]{4}[A-Z]{1}'
```



##javascript 

```
/d = [0-9]
/w = (a-z A-z 0-9...)
/s = space 
/t = tab
