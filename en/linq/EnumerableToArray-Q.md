# “EnumerableToArray” (Problem)

What will the following code display?

```cs
public static int CreateNumber(int x)
{
  Console.WriteLine("CreateNumber: " + x);
  return x;
}
public static IEnumerable<int> GetSmallNumbers()
{    
  yield return CreateNumber(1);
  yield return CreateNumber(2);
}
public static int[] GetArray()
{
  var numbers = GetSmallNumbers();
  foreach (var number in numbers)
    Console.WriteLine("GetArray:" + number);
  return numbers.ToArray();
}
void Main()
{
  GetArray();
}
```

[Solution](./EnumerableToArray-A.md)