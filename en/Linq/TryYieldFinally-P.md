# “TryYieldFinally” (Problem)

What will the following code display?

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

[Solution](./TryYieldFinally-S.md)