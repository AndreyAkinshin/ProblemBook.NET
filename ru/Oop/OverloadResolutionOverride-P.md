# «OverloadResolutionOverride» (Задача)

Что выведет следующий код?

```cs
class Foo
{
  public virtual void Quux(int a)
  {
    Console.WriteLine("Foo.Quux(int)");
  }
}
class Bar : Foo
{
  public override void Quux(int a)
  {
    Console.WriteLine("Bar.Quux(int)");
  }
  public void Quux(object a)
  {
    Console.WriteLine("Bar.Quux(object)");
  }
}
class Baz : Bar
{
  public override void Quux(int a)
  {
    Console.WriteLine("Baz.Quux(int)");
  }
  public void Quux<T>(params T[] a)
  {
    Console.WriteLine("Baz.Quux(params T[])");
  }
}
void Main()
{
  new Bar().Quux(42);
  new Baz().Quux(42);
}
```

[Решение](./OverloadResolutionOverride-S.md)