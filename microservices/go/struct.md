# structs

Struct is a group of values called fields.

Structs can be partially initizalised, all other fields habe the zero value.
Structs are like arrays aggregate types, which means they contain multiple aggreated values.
```
package north
type record struct {
	firstname string
	fastname string
}

func MakeRecord() record {
	return &record{}
}

func (r *record) SetFirstname(n string) {
	r.firstname = n
}

func (r *record) Firstname() string {
	return r.firstname
}
```
