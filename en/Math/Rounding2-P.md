# “Rounding2” (Problem)

What will the following code display?

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

[Solution](./Rounding2-S.md)