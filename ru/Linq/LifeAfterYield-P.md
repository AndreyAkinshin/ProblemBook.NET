# «LifeAfterYield» (Задача)

Что выведет следующий код?

```cs
IEnumerable<string> Foo()
{
  yield return "Bar";
  Console.WriteLine("Baz");
}
void Main()
{
  foreach (var str in Foo())
    Console.Write(str);
}
```

[Решение](./LifeAfterYield-S.md)