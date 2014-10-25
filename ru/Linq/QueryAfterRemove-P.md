# «QueryAfterRemove» (Задача)

Что выведет следующий код?

```cs
var list = new List<string> { "Foo", "Bar", "Baz" };
var query = list.Where(c => c.StartsWith("B"));
list.Remove("Bar");
Console.WriteLine(query.Count());
```

[Решение](./QueryAfterRemove-S.md)