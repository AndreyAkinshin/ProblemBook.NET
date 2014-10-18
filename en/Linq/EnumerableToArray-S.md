# “EnumerableToArray” (Solution)

```
GetString: Foo
EnumerableToArray: Foo
GetString: Bar
EnumerableToArray: Bar
GetString: Foo
GetString: Bar
```

LINQ queries use deferred/lazy execution. It means, a LINQ query without a cast method like [ToArray()](msdn.microsoft.com/library/vstudio/bb298736.aspx) or [ToList()](http://msdn.microsoft.com/library/vstudio/bb342261.aspx) is not executed immediately. The execution will be deferred until we do not explicitly require the results. Thus, the line

```cs
var strings = GetStringEnumerable();
```

will not print anything to the console. Next, in the loop

```cs
foreach (var s in strings)
  Console.WriteLine("EnumerableToArray: " + s);
```

query execution will be performed. Moreover, first will be evaluated the first `yield` (print `GetString: Foo`), next the loop body will be evaluated for the first enumerable element (print `EnumerableToArray: Foo`). Next, the `foreach` loop will require the second enumerable element, the second `yield` will be evaluated (print `GetString: Bar`), the loop body will be evaluated for the second element (print `EnumerableToArray: Bar`).

Next, the following line will be executed:

```cs
return strings.ToArray();
```

Our LINQ query will be performed again. So, the lines `GetString: Foo` and `GetString: Bar` will be printed again.

[Problem](./EnumerableToArray-P.md)