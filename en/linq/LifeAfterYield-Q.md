# “LifeAfterYield” (Problem)

What will the following code display?

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

[Solution](./LifeAfterYield-A.md)