# «ClosureAndForeach» (Решение)

## Ответ

C# 1.0 — C# 4.0: `3 3 3`

C# 5.0+: `1 2 3`

## Объяснение

В версиях C# 1.0 — C# 4.0 приведённый код превращался в следующую конструкцию:

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

Таким образом, все три элемента списка на самом деле являются одним и тем же делегатом, поэтому в консоли мы увидим три одинаковых значения, равных последнему значению `i`.

В С# 5.0+ произошли изменения, новый вариант кода:

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

Теперь каждый элемент списка ссылается на собственный делегат, так что все полученные значения будут разными.

[Задача](./ClosureAndForeach-P.md)