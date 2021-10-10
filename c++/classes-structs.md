# Klassen
```
class A
{
  int a; // private
  public:
    int b; // public
  private:
    int c; //private
}
```

x.h enthält Deklaration
```
class X
{
  public:
    int add(int a, int b);
};
```
x.cpp enthält Definition
```
int X::add(int a, int b) {
  return a + b;
}
```
# Structs
Structs sind wie Classes nur dass sie Standartmäßg public sind.
```
struct a
{
  int a; // public
}
```
