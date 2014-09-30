# «YieldExceptionYield» (Задача)
В какой момент произойдёт `Exception`?
```
public static IEnumerable<int> GetSmallNumbers()
{
  yield return 1;
  throw new Exception();
  yield return 2;
}
void Main()
{
  var numbers = GetSmallNumbers();
  var evenNumbers = numbers.Select(n => n * 2);
  Console.WriteLine(evenNumbers.FirstOrDefault());
}
```
[Решение](./YieldExceptionYield-A.md)
