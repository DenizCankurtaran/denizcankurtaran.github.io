# Functions

## Operator
"test" == "test" is possible.

## Join
```
strings.Join(os.Args[1:], " ")
```
## Split
```
strings.Split(names, '\n')
```

## Printf wildcars
 
| wildcard   | definition            |
| ---        | ---                   |
| %d         | decimal integer       |
| %x, %o, %b | floating point number |
| %t         | boolean               |
| %c         | rune (Unicode point)  |
| %s         | string                |
| %q         | quoted string         |
| %v         | any value             |
| %T         | type of any value     |
| %%         | percentage sign       |

```
fmt.Printf("type: %T value: %d", 4.123123123)
```
