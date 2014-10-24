# “ClosureAndForeach” (Problem)

C# 1.0 — C# 4.0: `3 3 3`

C# 5.0+: `1 2 3`

In C# 1.0 — C# 4.0, the code from the problem will be transformed in the following code:

```cs
public void Run()
{
  var actions = new List<Action>();
  DisplayClass c1 = new DisplayClass();
  foreach (int i in Enumerable.Range(1, 3))
  {
    с1.i = i;
    list.Add(c1.Action);
  }
  foreach (Action action in list)
    action();
}

private sealed class DisplayClass
{
  public int i;

  public void Action()
  {
    Console.WriteLine(i);
  }
}
```

Thus, all elements from the list refer to same delegate. So, we will see 3 same values in the console, they will equal the last value of `i`.

Some breaking changes were in C# 5.0. The new version of the code:

```cs
public void Run()
{
  var actions = new List<Action>();
  foreach (int i in Enumerable.Range(1, 3))
  {
    DisplayClass c1 = new DisplayClass();
    с1.i = i;
    list.Add(c1.Action);
  }
  foreach (Action action in list)
    action();
}

private sealed class DisplayClass
{
  public int i;

  public void Action()
  {
    Console.WriteLine(i);
  }
}
```

Now, each element of the list refers to own delegate, all printed values will be different.

[Solution](./ClosureAndForeach-P.md)