# Net/http package

net/http contains internet access tools.

## fetch example
```
resp, err := http.Get(url)
body, err := ioutil.ReadAll(resp.Body)
resp.Body.Close()

```

## API example
```
func main() {
  http.HandleFunc("/", handler)
  http.ListenAndServe("localhost:8000", nil)
}

func handler(w http.ResponseWriter, r *http.Request){
  fmt.Fprintf(w, "URL.PATH=%q\n", r.URL.Path)
}
```
