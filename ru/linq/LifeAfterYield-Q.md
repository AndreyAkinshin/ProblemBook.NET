# «LifeAfterYield» (Задача)

Что выведет следующий код?

```cs
public IEnumerable<int> Foo()
{
  yield return 1;
  Console.WriteLine("Foo");
}
void Main()
{
  foreach (var i in Foo())
    Console.Write(i);
}
```

[Решение](./LifeAfterYield-A.md)