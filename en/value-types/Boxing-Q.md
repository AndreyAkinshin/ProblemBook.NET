# “Boxing” (Problem)
What will the following code display?
```cs
struct Foo
{   
  int value;
  public override string ToString()
  { 
    if (value == 2)
      return "Baz";
    return (value++ == 0) ? "Foo" : "Bar";
  }
}
void Main()
{ 
  var foo = new Foo();
  Console.WriteLine(foo);
  Console.WriteLine(foo);
  object bar = foo;
  object qux = foo;
  object baz = bar;
  Console.WriteLine(baz);
  Console.WriteLine(bar);
  Console.WriteLine(baz);
  Console.WriteLine(qux);
}
```
[Solution](./Boxing-A.md)
