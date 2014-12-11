# «TryYieldFinally» (Задача)

Что выведет следующий код?

```cs
public static IEnumerable<int> GetSmallNumbers()
{
  try
  {
    yield return 1;
    yield return 2;
  }
  finally
  {
    Console.WriteLine("Foo");
  }
}
void Main()
{
  Console.WriteLine(GetSmallNumbers().First());
}
```

[Решение](./TryYieldFinally-S.md)