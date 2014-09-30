# «Rounding1» (Задача)

Что выведет следующий код?

```cs
Console.WriteLine(
  "| Number | Round | Floor | Ceiling | Truncate | Format |");
foreach (var x in new[] { -2.9, -0.5, 0.3, 1.5, 2.5, 2.9 })
{
  Console.WriteLine(string.Format(CultureInfo.InvariantCulture,
    "| {0,6} | {1,5} | {2,5} | {3,7} | {4,8} | {0,6:N0} |",
    x, Math.Round(x), Math.Floor(x),
    Math.Ceiling(x), Math.Truncate(x)));
}
```

[Решение](./Rounding1-A.md)