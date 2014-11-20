# “LockSlimInFinalizer” (Problem)

What will the following code display?

```cs
class Foo
{
  private readonly ReaderWriterLockSlim lockSlim;

  public Foo(ReaderWriterLockSlim lockSlim)
  {
    this.lockSlim = lockSlim;
    lockSlim.EnterReadLock();
  }
  
  ~Foo()
  {
    Console.WriteLine("~Foo: start");
    try
    {
      if (lockSlim != null)
        lockSlim.ExitReadLock();
    }
    catch (Exception e)
    {
      Console.WriteLine("Exception: " + e.GetType().Name);
    }
    Console.WriteLine("~Foo: finish");
  }
}
void Main()
{
  var foo = new Foo(new ReaderWriterLockSlim());
  GC.Collect();
  GC.WaitForPendingFinalizers();
}
```

[Solution](./LockSlimInFinalizer-S.md)