# “StaticFieldOfGeneric” (Problem)

What will the following code display?

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

[Solution](./StaticFieldOfGeneric-S.md)