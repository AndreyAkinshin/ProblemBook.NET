# «QueryWithInc» (Задача)
Что выведет следующий код?
```cs
int Inc(int x)
{
  Console.WriteLine("Inc: " + x);
  return x + 1;
}
void Main()
{
  var numbers = Enumerable.Range(0, 10);
  var query =
    (from number in numbers
     let number2 = Inc(number)
     where number2 % 2 == 0
     select number2).Take(2);
  foreach (var number in query)
    Console.WriteLine("Number: " + number);
}
```
[Решение](./QueryWithInc-A.md)
