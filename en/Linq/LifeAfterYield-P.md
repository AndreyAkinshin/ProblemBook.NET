# “LifeAfterYield” (Problem)

What will the following code display?

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

[Solution](./LifeAfterYield-S.md)