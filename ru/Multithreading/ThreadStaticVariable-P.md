# «ThreadStaticVariable» (Задача)

Что выведет следующий код?

```cs
[ThreadStatic]
static readonly int Foo = 42;

void Main()
{
  var thread = new Thread(() => Console.WriteLine(Foo));
  thread.Start();
  thread.Join();
}
```

[Решение](./ThreadStaticVariable-S.md)