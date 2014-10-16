# «EnumerableToArray» (Задача)

Что выведет следующий код?

```cs
public static string GetString(string s)
{
  Console.WriteLine("GetString: " + s);
  return s;
}
public static IEnumerable<string> GetStringEnumerable()
{    
  yield return GetString("Foo");
  yield return GetString("Bar");
}
public static string[] EnumerableToArray()
{
  var strings = GetStringEnumerable();
  foreach (var s in strings)
    Console.WriteLine("EnumerableToArray: " + s);
  return strings.ToArray();
}
void Main()
{
  EnumerableToArray();
}
```

[Решение](./EnumerableToArray-A.md)