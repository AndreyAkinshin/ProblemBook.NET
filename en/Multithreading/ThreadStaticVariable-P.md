# “ThreadStaticVariable” (Problem)

What will the following code display?

```cs
[ThreadStatic]
static int Foo = 42;

void Main()
{
  var thread = new Thread(() => Console.WriteLine(Foo));
  thread.Start();
  thread.Join();
}
```

[Solution](./ThreadStaticVariable-S.md)