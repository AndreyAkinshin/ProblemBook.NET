# “CorruptedNumber” (Solution)

You can use custom `CultureInfo`:

```cs
var culture = (CultureInfo) CultureInfo.InvariantCulture.Clone();
culture.NumberFormat.NegativeSign = "Foo";
Thread.CurrentThread.CurrentCulture = culture;
Console.WriteLine(-42); // Displays "Foo42"
```

[Problem](./CorruptedNumber-Q.md)