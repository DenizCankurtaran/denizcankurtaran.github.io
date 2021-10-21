Wie java wildcards
# Classen/ Struct
## Parameter
 - Typ Parameter
    - Float ...
 - Nicht Typ Parameter
    - Integrale Werte
    - Zeigerwerte
 - Template-Template-Parameter
    - Template als Parameter

## Deduzierte Type
```
template <auto N>
```

## Variadisches Template
```
template <int Ns...>

template<typename ... Args>
Vec<T, N>::Vec(const T& first, const Args& ... rest)
  : v_({first, rest...})
{
    static_assert(N == 1 + sizeof...(Args), "Vec: wrong number of arguments");
}
Vec<float, 3> vec(1f, 2f, 3f);
```
## Beispiele:
Basics:
```
template <typname T>
class X {}
```
Example 1:
```
template<typename T, int N = 100>
class Fifo {
  std::array<T, N> data_;
}
```
Template Template
```
template<template<typname> class V>
```

# Funktionen
```
template<typename T>
T mult(T const& v1, T const& v2) {
  return v1 * v2
}

mult<int>(1, 4)
mult(7.0, 2.0)
```
