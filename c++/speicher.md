# Allokation und Konstruktion
```
void* memory = malloc(sizeof(Obj));

Obj* obj = new(memory) Obj(1, 2, 3);
```
```
void* memory = malloc(sizeof(float) * 10); // speicher für 10 floats reserviert
```

```
Obj* obj = static_cast<Obj*>(malloc(obj));
Obj* obj = new(obj) Obj(1, 2, 3);

obj->~Obj();
free(obj);
```

