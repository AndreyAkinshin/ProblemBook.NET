# “QueryAfterRemove” (Problem)

What will the following code display?

```cs
var list = new List<string> {"A", "BB", "CCC"};
var query = list.Where(c => c.Length == 2);
list.Remove("BB");
Console.WriteLine(query.Count());
```

[Solution](./QueryAfterRemove-A.md)