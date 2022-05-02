

function isEmailValid(email) {
  const emailRegexp = new RegExp(
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  )

  return emailRegexp.test(email)
}

console.log(isEmailValid('helloitsme@herewecode.io')) // true
console.log(isEmailValid('hello-its-me@herewecode.io')) // true
console.log(isEmailValid('hello.its.me@herewecode.io')) // true
console.log(isEmailValid('helloitsme+test@herewecode.io')) // true
console.log(isEmailValid('.helloitsme@herewecode.io')) // false
console.log(isEmailValid('helloitsme.@herewecode.io')) // false
console.log(isEmailValid('@herewecode.io')) // false
console.log(isEmailValid('helloitsmeherewecode.io')) // false
console.log(isEmailValid('helloitsme@herewecode')) // false
console.log(isEmailValid('d@d.o')) // false
