# «Enumerator» (Задача)
Что выведет следующий код?
```cs
var x = new 
  {
    Items = new List<int> { 1, 2, 3 }.GetEnumerator()
  };
while (x.Items.MoveNext())
  Console.WriteLine(x.Items.Current);
```
[Решение](./Enumerator-A.md)
