# “ExplicitlyInternment” (Problem)

What will the following code display?

```cs
var x = "AB";
var y = new StringBuilder().Append('A').Append('B').ToString();
var z = string.Intern(y);
Console.WriteLine(x == y);
Console.WriteLine(x == z);
Console.WriteLine((object)x == (object)y);
Console.WriteLine((object)x == (object)z);
```

[Solution](./ExplicitlyInternment-A.md)