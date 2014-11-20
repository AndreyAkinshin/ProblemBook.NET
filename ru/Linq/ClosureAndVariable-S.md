# «ClosureAndVariable» (Решение)

## Ответ

```
2
```

## Объяснение

Приведённый код примет следующий вид:

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

Выполнение запроса начнётся только в самой последней строчке кода. Как можно видеть, для обоих замыканий создался один и тот же вспомогательный класс. Сначала выполнится первый запрос `list2.Where(displayClass.Method1)` и вернёт `{ "Bar", "Baz" }`, т.к. `displayClass.startLetter` к моменту исполнения равна `"B"`. Далее выполнится запрос `source.Where(displayClass.Method2)`, который также вернёт `{ "Bar", "Baz" }`. Количество элементов в результате равно двум.

[Задача](./ClosureAndVariable-P.md)