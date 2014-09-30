# «DivideByZero» (Задача)

Что выведет следующий код?

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

[Решение](./DivideByZero-A.md)