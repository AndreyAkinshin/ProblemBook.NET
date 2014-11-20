# «CorruptedNumber» (Решение)

## Ответ

Задание можно выполнить с использованием пользовательской локали:

```cs
var culture = (CultureInfo) CultureInfo.InvariantCulture.Clone();
culture.NumberFormat.NegativeSign = "Foo";
Thread.CurrentThread.CurrentCulture = culture;
Console.WriteLine(-42); // Displays "Foo42"
```

[Задача](./CorruptedNumber-P.md)