# “Enumerator” (Problem)

What will the following code display?

```cs
var x = new 
  {
    Items = new List<int> { 1, 2, 3 }.GetEnumerator()
  };
while (x.Items.MoveNext())
  Console.WriteLine(x.Items.Current);
```

[Solution](./Enumerator-A.md)