# “Eps” (Solution)

## Answer

```
0.1 + 0.2 != 0.3
```

## Explanation

The `Double` numbers use the [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point) specification and they are stored in 64-bit binary format. Unfortunately, most decimal non-integer numbers can not be represented in the binary format. This fact affects affects to performing of arithmetic operations with floating-point numbers:

```cs
// Displays '5.5511151231257827E-17'
Console.WriteLine("{0:R}", 0.1+0.2-0.3);
```

The proper way to compare `double` numbers is comparing with some epsilon. An example:

```cs
public static void IsEqual(double a, double b, double eps = 1e-9)
{
    return Math.Abs(a - b) < 1e-9
}
```

[Problem](./Eps-P.md)