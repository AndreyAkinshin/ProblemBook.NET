# “ClosureAndVariable” (Solution)

## Answer

```
2
```

## Explanation

The code is translated into the following form:

```cs
class DisplayClass
{
  public string startLetter;

  public bool Method1(string c)
  {
    return c.StartsWith(this.startLetter);
  }

  public bool Method2(string c)
  {
    return c.StartsWith(this.startLetter);
  }
}

void Main()
{
  DisplayClass displayClass = new DisplayClass();
  var list1 = new List<string> { "Foo", "Bar", "Baz" };
  var list2 = list1;
  displayClass.startLetter = "F";
  IEnumerable<string> source = list2.Where(displayClass.Method1);
  displayClass.startLetter = "B";
  Console.WriteLine(source.Where(displayClass.Method2).Count());
}
```

The execution of the LINQ queries will start only in the last line of code. As can be seen, the same helper class creates for both queries. First, the `list2.Where(displayClass.Method1)` query will be executed. It returns `{ "Bar", "Baz" }` because `displayClass.startLetter` at the time of execution is `"B"`. Next, the `source.Where(displayClass.Method2)`  query will be executed. It also returns `{ "Bar", "Baz" }`. The number of elements in the result is two.

[Problem](./ClosureAndVariable-P.md)