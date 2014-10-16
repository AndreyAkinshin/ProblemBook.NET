# «EnumerableToArray» (Решение)

```
GetString: Foo
EnumerableToArray: Foo
GetString: Bar
EnumerableToArray: Bar
GetString: Foo
GetString: Bar
```

LINQ-запросы являются ленивыми, т.е. реализуют отложенное исполнение. Это означает, что если сфомировать запрос и не вызвать для него явно метод вроде [ToArray()](msdn.microsoft.com/library/vstudio/bb298736.aspx) или [ToList()](http://msdn.microsoft.com/library/vstudio/bb342261.aspx), то выполнение запроса будет отложено до того момента, пока мы явно не затребуем результатов. Таким образом, строка

```cs
var strings = GetStringEnumerable();
```

не выведет на консоль ничего. Далее, в цикле

```cs
foreach (var s in strings)
  Console.WriteLine("EnumerableToArray: " + s);
```

произойдёт выполнение запроса. Причём, сначала выполнится первый `yield` (вывод строки `GetString: Foo`), а после него выполнится тело цикла для первого значения перечисления (вывод строки `EnumerableToArray: Foo`). Далее, цикл `foreach` запросит второй элемент перечисления, будет выполнен второй `yield` (вывод строки `GetString: Bar`) и второй раз будет выполнено тело цикла для полученного элемента (вывод строки `EnumerableToArray: Bar`).

Далее следует строка

```cs
return strings.ToArray();
```

Тут можно наблюдать повторное исполнение LINQ-запроса, а значит мы вновь произойдёт вывод строк `GetString: Foo` и `GetString: Bar`.

[Задача](./EnumerableToArray-Q.md)