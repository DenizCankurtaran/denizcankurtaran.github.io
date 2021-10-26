Funktion besteht aus Signatur und Body

## Signatur
```
returntyp name (parameter);
auto foo(Typ1 wert) -> returntyp;
```
generisch
```
template<typename T>
auto foo (T wert, ...) -> decltype(Expr. abhängig von T); 
```

## Lambda
```
auto sqr = [](int x) {return x * x;};
```
```
int y = 1;;
auto add = [y](int x) {return x + y;}; kopiert y in das lambda
auto add = [&y](int x) {return x + y;}; erhälrt referenz von y
auto add = [&](int x) {return x + y;}; gesamter kontext per referenz
auto add = [=](int x) {return x + y;}; gesamter kontext als kopie
```

## generische Lambdas
```
auto add = [](auto x, auto y) {return x + y;};
```

## Const
const keyword nach funktionsname => not mutatable

## Inline
triviale kleine funktion? Funktionsoptimierung?
Kein echter Funktionsaufruf.


## mehrere rückgabewerte
```
std::tuple<int, float float>
foo();

auto[n, t1, t2] = foo();

```

## Beispiel
```
int add(int a, int b) {
  return a + b;
}
```

