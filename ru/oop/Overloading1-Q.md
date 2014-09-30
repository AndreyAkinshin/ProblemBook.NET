# «Overloading1» (Задача)

Что выведет следующий код?

```cs
void Foo(object a)
{
  Console.WriteLine("object");
}
void Foo(object a, object b)
{
  Console.WriteLine("object, object");
}
void Foo(params object[] args)
{
  Console.WriteLine("params object[]");
}
void Foo<T>(params T[] args)
{
  Console.WriteLine("params T[]");
}
class Bar { }
void Main()
{
  Foo();
  Foo(null);
  Foo(new Bar());
  Foo(new Bar(), new Bar());
  Foo(new Bar(), new object());
}
```

[Решение](./Overloading1-A.md)