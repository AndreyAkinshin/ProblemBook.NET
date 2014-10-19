# «OverloadResolutionBasic» (Решение)

```
params object[]
params object[]
params T[]
params T[]
object, object
```

Итак, у нас имеются методы:

* `void Foo(object a)` -> `object`
* `void Foo(object a, object b)` -> `object, object`
* `void Foo(params object[] args)` -> `params object[]`
* `void Foo<T>(params T[] args)` -> `params T[]`

Рассмотрим каждый вызов отдельно.

* `Foo()` -> `params object[]`

Варианты `object` и `object, object` не подходят по количеству аргументов. Вариант `params T[]` не подходит, т.к. невозможно определить тип `T`. Таким образом, правильный вариант — `params object[]`.

* `Foo(null)` -> `params object[]`

Вариант `object, object` не подходит по количеству аргументов. Вариант `params T[]` не подходит, т.к. невозможно определить тип `T`. Вариант `params object[]` подходит в `expanded` и `unexpanded` формах, в этом случае мы выбираем `expanded`-форму, т.е. сигнатура будет выглядеть как `Foo(object[] args)`. Из двух оставшихся вариантов `object` и `object[]` компилятор выберет более специфичный, т.е. `object[]` (он же `params object[]`).

* `Foo(new Bar())` -> `params T[]`

Вариант `object, object` не походит по количеству элементов. Варианты `object` и `params object[]` будут требовать дополнительной конвертации `Bar` в `object`, поэтому вариант `params T[]` (который, по сути, становится `params Bar[]`) более предпочтителен.

* `Foo(new Bar(), new Bar())` -> `params T[]`

Вариант `object` не подходит по количеству элементов. Варианты `object` и `params object[]` будут требовать дополнительной конвертации `Bar` в `object`, поэтому вариант `params T[]` (который, по сути, становится `params Bar[]`) более предпочтителен.

* `Foo(new Bar(), new object())` -> `object, object`
Вариант `object` не подходит по количеству элементов. Среди оставшихся вариантов существует ровно одна версия без `params`: `object, object`. Она будет более предпочтительна.

См. также:

* [«Overload resolution»](http://msdn.microsoft.com/library/aa691336.aspx), [«Method invocations»](msdn.microsoft.com/library/aa691356.aspx), [«Applicable function member»](http://msdn.microsoft.com/en-US/library/aa691337.aspx) в MSDN
* Глава [«Overloading»](http://csharpindepth.com/Articles/General/Overloading.aspx) в книге [«C# in Depth»](http://csharpindepth.com/)

[Задача](./OverloadResolutionBasic-P.md)