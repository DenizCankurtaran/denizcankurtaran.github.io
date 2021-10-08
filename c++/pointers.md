# Pointer
Ein Pointer ist ein Integer, der eine *Memory Address* speichert.
```
int*
```

```
int var = 8;
int* ptr = &var;

*ptr = 10;
LOG(var)  // 10
```

## Pointer Beispiel

```
void Increment(int* value) 
{
  (*value)++;
  // *value => zeigt auf die Memory Address, die Klammern, für Reihenfolge
}
```
```
int a = 5;
Increment(&a); // Pointer auf Memory Address
LOG(a);
```

# Reference
Eine Reference ist wie ein Alias für eine Variable. (Normales Java Verhalten)
```
int&
```

```
int a = 5;
int& ref = a;
ref = 2;

LOG(a)  // 2
```

## Reference Beispiel

```
void Increment(int& value)
{
  value++;
}
```
```
int a = 5;
Increment(a);
LOG(a);
```
