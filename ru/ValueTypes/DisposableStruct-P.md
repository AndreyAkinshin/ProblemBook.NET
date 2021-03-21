# “Disposable Struct” (Задача)

Что выведет следующий код?

```cs
static void Main()
{
  var foo = new Foo();

  using (foo)
  {
    foo.PrintFoo();
  }

  Console.WriteLine(foo.Disposed);
}


struct Foo : IDisposable
{
  public bool Disposed { get; private set; }
        
  public void Dispose()
  {
    Disposed = true;
  }

  public void PrintFoo()
  {
    Console.WriteLine("Foo");
  }
}
```

[Решение](./DisposableStruct-S.md)