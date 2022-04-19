## Notes  on regex

MetaCharacters:
[] . ^ $ * + ? {} () \ |
_________________________________________________

^ : start 
$ : end 
[] : character set 
[^] : negation
(|) : or operator
(\) : CHARACTER IS not threaten in any way 
(*) : matches zero or more occurrences of the pattern left to it
(+) : matches one or more occurrences of the pattern left to it
(?) : matches zero or one occurrence of the pattern left to it
{n,m} : This means at least n, and at most m repetitions of the pattern left to it.


Reference link [click here :](https://www.programiz.com/python-programming/regex)


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
'^[0-9]{2,3}$'
```

### pin code validation

```
'^[0-9]{6}$'
```

### Pan number validation

```
'[A-Z]{5}[0-9]{4}[A-Z]{1}'
```


