# Klassen

## Konstruktoren
Initialisierer Liste
```
Vec2::Vec2(float x, float y)
  : x_(x), y_(y)
{}
```

## Concrete Types
*behaves like an int*
```
Vec2 Vec2::operator-() const
{
  return Vec2(-x(), -y());
}
```
```
Vec2 c = -b;
```
## = operator
```
Vec2& Vec2::operator=(const Vec2& rhs)
{
  x_ = rhs.x_;
  y_ = rhy.y_;
  return *this;
}
```

## Friend
friend keyword ermöglicht zugriff auf private Attribute

## Default Werte
in Deklaration
Vec2.h
```
Vec2(float x=0, float y=0);
```

## Accessor
const keyword nach funktionsname => not mutatable \
getter

## Mutator
setter


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
## Structs
Structs sind wie Classes nur dass sie Standartmäßg public sind.
```
struct a
{
  int a; // public
}
```
