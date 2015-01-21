# «StaticFieldOfGeneric» (Задача)

Что выведет следующий код?

```cs
class Foo<T>
{
  public static int Bar;
}
void Main()
{
  Foo<int>.Bar++;
  Console.WriteLine(Foo<double>.Bar);
}
```

[Решение](./StaticFieldOfGeneric-S.md)