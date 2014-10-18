# “DivideByZero” (Problem)

What will the following code display?

```cs
var zero = 0;
try
{
  Console.WriteLine(42 / 0.0);
  Console.WriteLine(42.0 / 0);
  Console.WriteLine(42 / zero);
}
catch (DivideByZeroException)
{
  Console.WriteLine("DivideByZeroException");
}
```

[Solution](./DivideByZero-S.md)