# Goroutines

1. A goroutine is a concurrent function.
2. A Channel is a communication mechanism between routines
  - Main is a goroutine
  - `go` creates new goroutines
3. When sending/ receiving, the routine blocks, until the corresponding operation occured. 

A channel of strings
```
ch := make(chan string)
```

## Example
```
func routine(ch chan <- string){
  start := time.Now()
  time.Sleep(time.Second)
  ch <- fmt.Sprintf("elapsed time: %f", time.Since(start).Seconds())
}

func main() {
  ch := make(chan string)
  for i:=0; i < 10; i++ {
    go routine(ch)

}
for i:=0; i < 10; i++ {
    fmt.Println(<- ch)
  }
}

```
