# “YieldExceptionYield” (Solution)

## Answer

Exception is not going to happen.

## Explanation

Indeed, the line

```cs
var numbers = GetSmallNumbers();
```

is only building a query, but does not execute it. The line

```cs
var evenNumbers = numbers.Select(n => n * 2);
```

is also only building another query without direct execution. Let's look to the last list of the `Main` method:

```cs
Console.WriteLine(evenNumbers.FirstOrDefault());
```

This call will get only the first element of the result enumerable (single call of `MoveNext()` and `Current` will be executed). Evaluation of the next elements will nor occur. Thus, the code will work without any exceptions.

[Problem](./YieldExceptionYield-P.md)