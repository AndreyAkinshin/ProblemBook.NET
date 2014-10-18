# “Rounding1” (Problem)

What will the following code display?

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

[Solution](./Rounding1-S.md)