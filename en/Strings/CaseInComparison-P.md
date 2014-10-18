# “CaseInComparison” (Problem)

Are the following methods of comparison term `a` and` b` insensitive equivalent:

```cs
Console.WriteLine(
  string.Compare(a.ToUpper(), b.ToUpper()));
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase));
```

[Solution](./CaseInComparison-S.md)