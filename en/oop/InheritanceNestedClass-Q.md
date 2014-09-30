# “InheritanceNestedClass” (Problem)

What will the following code display?

```cs
class Foo
{
  protected class Quux
  {
    public Quux()
    {
      Console.WriteLine("Foo.Quux()");
    }
  }
}
class Bar : Foo
{
  new class Quux
  {
    public Quux()
    {
      Console.WriteLine("Bar.Quux()");
    }
  }
}
class Baz : Bar
{
  public Baz()
  {
    new Quux();
  }
}
void Main()
{
  new Baz();
}
```

[Solution](./InheritanceNestedClass-A.md)