# Conditionales

## normal if
```
err := foo()
if err != nil {
  fmt.Printf("%s\n", err)
}
```
## shorter if with smaller scope on err
```
if err := foo(); err != nil {
  fmt.Printf("%s\n", err)
}
```
