# «StringPlusNull» (Задача)

Что выведет следующий код?

```cs
try
{
  Console.WriteLine(((string)null + null + null) == null);
}
catch (Exception e)
{
  Console.WriteLine(e.GetType());
}
```

[Решение](./StringPlusNull-S.md)