# Variables

Go does not allow unused local variables. If such a case happens use `_`.
Initilization without declaration, uses empty declaration.

Example:
```
var s string // s = ""
s := ""
var s = ""
vas s string = ""
```

`s:= ""` can only be used inside functions, not on a package level

## Scope

Var and const variables can be decalared in package or function scope.

## Constants

The value of a const can be a
 - String
 - Boolean
 - Number

