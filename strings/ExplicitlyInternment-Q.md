# «ExplicitlyInternment» (Задача)
Что выведет следующий код?
```cs
var x = "AB";
var y = new StringBuilder().Append('A').Append('B').ToString();
var z = string.Intern(y);
Console.WriteLine(x == y);
Console.WriteLine(x == z);
Console.WriteLine((object)x == (object)y);
Console.WriteLine((object)x == (object)z);
```
[Решение](./ExplicitlyInternment-A.md)
