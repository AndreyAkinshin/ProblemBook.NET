# “LifeAfterYield” (Solution)

```
BarBaz
```

The code from the problem will be transformed in the following code (some part of the code specifically removed for better understanding):

```cs
private sealed class FooEnumerable : 
    IEnumerable<string>, IEnumerator<string>
{
  private int state;
  public string Current { get; private set; }

  object IEnumerator.Current
  {
    get { return Current; }
  }

  public FooEnumerable(int state)
  {
    this.state = state;
  }

  public IEnumerator<string> GetEnumerator()
  {
    FooEnumerable fooEnumerable;
    if (state == -2)
    {
      state = 0;
      fooEnumerable = this;
    }
    else
      fooEnumerable = new FooEnumerable(0);
    return fooEnumerable;
  }

  IEnumerator IEnumerable.GetEnumerator()
  {
    return GetEnumerator();
  }

  bool IEnumerator.MoveNext()
  {
    switch (state)
    {
      case 0:
        Current = "Bar";
        state = 1;
        return true;
      case 1:
        state = -1;
        Console.WriteLine("Baz");
        break;
    }
    return false;
  }

  void IEnumerator.Reset()
  {
    throw new NotSupportedException();
  }

  void IDisposable.Dispose()
  {
  }
}

IEnumerable<string> Foo()
{
  return new FooEnumerable(-2);
}

void Main()
{
  var enumerator = Foo().GetEnumerator();
  while (enumerator.MoveNext())
    Console.Write(enumerator.Current);
}
```

[Problem](./LifeAfterYield-P.md)