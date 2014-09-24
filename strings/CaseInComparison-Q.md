# «CaseInComparison» (Задача)
Являются ли следующие способы сравнения срок `a` и `b` без учёта регистра эквивалентными:
```cs
Console.WriteLine(
  string.Compare(a.ToUpper(), b));
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase));
```
[Решение](./CaseInComparison-A.md)
