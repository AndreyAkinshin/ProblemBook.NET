# “QueryWithInc” (Solution)

## Answer

```
Inc: 0
Inc: 1
Number: 2
Inc: 2
Inc: 3
Number: 4
```

## Explanation

An imperative version of the code is as follows:

```cs
var numbers = new[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
var takenAmount = 0;
for (int i = 0; i < numbers.Length; i++)
{
  var number = numbers[i];
  Console.WriteLine("Inc: " + number);
  var number2 = number + 1;
  if (number2 % 2 == 0)
  {
    Console.WriteLine("Number: " + number2);
    takenAmount++;
    if (takenAmount == 2)
      break;
  }
}
```

[Problem](./QueryWithInc-P.md)