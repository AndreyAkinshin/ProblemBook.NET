# «ClosureAndForeach» (Решение)

## Ответ

В старых версиях компиляторов: `3 3 3`.

В новых версиях компиляторов: `1 2 3`.

## Объяснение

В старых версиях компиляторов приведённый код превращался в следующую конструкцию:

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

В современных версиях компиляторов произошли изменения, новый вариант кода:

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

Примеры:

```
Mono compiler 2.4.4                       : 3 3 3
Mono compiler 3.10.0                      : 1 2 3
Mono compiler 3.10.0        langversion=4 : 1 2 3
MS compiler 3.5.30729.7903                : 3 3 3
MS compiler 4.0.30319.1                   : 3 3 3
MS compiler 4.0.30319.33440               : 1 2 3
MS compiler 4.0.30319.33440 langversion=4 : 1 2 3
```

## Ссылки

* [ItDepends.NET: ClosureAndForeach](https://github.com/AndreyAkinshin/ItDepends.NET/tree/master/ClosureAndForeach)
* [Eric Lippert: Closing over the loop variable considered harmful](http://blogs.msdn.com/b/ericlippert/archive/2009/11/12/closing-over-the-loop-variable-considered-harmful.aspx)
* [Eric Lippert: Closing over the loop variable, part two](http://blogs.msdn.com/b/ericlippert/archive/2009/11/16/closing-over-the-loop-variable-part-two.aspx)

[Задача](./ClosureAndForeach-P.md)