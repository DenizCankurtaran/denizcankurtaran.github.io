# Pointer

& before a variable points to the memory address.
*before a parameter resolves the address.

```
func pointerTest(a *int) {
  fmt.Println(a) //memory address
  *a++
}

func main(){
  var a int // 0
  pointerTest(&a)
  fmt.Println(a) // 1
}
```
