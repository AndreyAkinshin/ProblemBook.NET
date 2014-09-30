# “Closure” (Problem)
What will the following code display?
```cs
var actions = new List<Action>();
foreach (var i in Enumerable.Range(1, 3))
  actions.Add(() => Console.WriteLine(i));
foreach (var action in actions)
  action();
```
[Solution](./Closure-A.md)
