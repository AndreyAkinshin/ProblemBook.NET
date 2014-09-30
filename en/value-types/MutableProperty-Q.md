# “MutableProperty” (Problem)
What will the following code display?
```cs
public struct Foo
{
  public int Value;
  public void Change(int newValue)
  {
    Value = newValue;
  }
}
public class Bar
{
  public Foo Foo { get; set; }
}
void Main()
{
  var bar = new Bar { Foo = new Foo() };
  bar.Foo.Change(5);
  Console.WriteLine(bar.Foo.Value);
}
```
[Solution](./MutableProperty-A.md)
