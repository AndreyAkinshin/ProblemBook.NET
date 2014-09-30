# «QueryAfterRemove» (Задача)

Что выведет следующий код?

```cs
var list = new List<string> {"A", "BB", "CCC"};
var query = list.Where(c => c.Length == 2);
list.Remove("BB");
Console.WriteLine(query.Count());
```

[Решение](./QueryAfterRemove-A.md)