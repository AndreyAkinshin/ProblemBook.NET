# “QueryAfterRemove” (Problem)

What will the following code display?

```cs
var list = new List<string> { "Foo", "Bar", "Baz" };
var query = list.Where(c => c.StartsWith("B"));
list.Remove("Bar");
Console.WriteLine(query.Count());
```

[Solution](./QueryAfterRemove-S.md)