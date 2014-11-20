# “ExceptionYieldYield” (Solution)

## Answer

Call of `evenNumbers.FirstOrDefault()`.

## Explanation

The lines

```cs
var numbers = GetSmallNumbers();
var evenNumbers = numbers.Select(n => n * 2);
```

only build a query, but don't execute it. A logic of the `GetSmallNumbers()` method starts run at the first call of the `MoveNext()` method, which corresponds to the first call of the `MoveNext()` method. At this point, the `Exception` will happen.

[Problem](./ExceptionYieldYield-P.md)