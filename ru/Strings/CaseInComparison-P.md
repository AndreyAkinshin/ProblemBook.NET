# «CaseInComparison» (Задача)

Являются ли следующие способы сравнения строк `a` и `b` без учёта регистра эквивалентными:

```cs
Console.WriteLine(
  string.Compare(a.ToUpper(), b.ToUpper()));
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase));
```

[Решение](./CaseInComparison-S.md)
