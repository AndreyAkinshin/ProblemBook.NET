# “ClosureAndVariable” (Problem)

What will the following code display?

```cs
var list = new List<string> { "Foo", "Bar", "Baz" };
var startLetter = "F";
var query = list.Where(c => c.StartsWith(startLetter));
startLetter = "B";
query = query.Where(c => c.StartsWith(startLetter));
Console.WriteLine(query.Count());
```

[Solution](./ClosureAndVariable-S.md)