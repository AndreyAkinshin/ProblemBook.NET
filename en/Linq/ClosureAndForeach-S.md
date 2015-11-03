# “ClosureAndForeach” (Solution)

## Answer

In old compiler versions: `3 3 3`.

In new compiler versions: `1 2 3`.

## Explanation

In old compiler versions, the code from the problem will be transformed in the following code:

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

Some breaking changes were in new compiler versions. The new version of the code:

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

Examples:

```
Mono compiler 2.4.4                       : 3 3 3
Mono compiler 3.10.0                      : 1 2 3
Mono compiler 3.10.0        langversion=4 : 1 2 3
MS compiler 3.5.30729.7903                : 3 3 3
MS compiler 4.0.30319.1                   : 3 3 3
MS compiler 4.0.30319.33440               : 1 2 3
MS compiler 4.0.30319.33440 langversion=4 : 1 2 3
```

## Links

* [ItDepends.NET: ClosureAndForeach](https://github.com/AndreyAkinshin/ItDepends.NET/tree/master/ClosureAndForeach)
* [Eric Lippert: Closing over the loop variable considered harmful](http://blogs.msdn.com/b/ericlippert/archive/2009/11/12/closing-over-the-loop-variable-considered-harmful.aspx)
* [Eric Lippert: Closing over the loop variable, part two](http://blogs.msdn.com/b/ericlippert/archive/2009/11/16/closing-over-the-loop-variable-part-two.aspx)

[Problem](./ClosureAndForeach-P.md)