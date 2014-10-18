# «Rounding2» (Задача)

Что выведет следующий код?

```cs
Action<int,int> print = (a, b) =>
  Console.WriteLine("{0,2} = {1,2} * {2,3}   + {3,3}  ",
                    a, b, a/b, a%b);
Console.WriteLine(" a =  b * (a/b) + (a%b)");
print(7, 3);
print(7, -3);
print(-7, 3);
print(-7, -3);
```

[Решение](./Rounding2-S.md)