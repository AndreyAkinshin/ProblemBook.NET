# «Closure» (Задача)
Что выведет следующий код?
```cs
var actions = new List<Action>();
foreach (var i in Enumerable.Range(1, 3))
  actions.Add(() => Console.WriteLine(i));
foreach (var action in actions)
  action();
```
[Решение](./Closure-A.md)
