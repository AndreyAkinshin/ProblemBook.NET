# “ClouseAndVariable” (Problem)

What will the following code display?

```cs
var list = new List<string> {"A", "BB", "CCC"};
var minLength = 3;
var query = list.Where(c => c.Length >= minLength);
minLength = 2;
query = query.Where(c => c.Length >= minLength);
Console.WriteLine(query.Count());
```

[Solution](./ClouseAndVariable-A.md)