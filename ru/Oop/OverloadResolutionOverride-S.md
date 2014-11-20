# «OverloadResolutionOverride» (Решение)

## Ответ

```
Bar.Quux(object)
Baz.Quux(params T[])
```

## Объяснение

Есть такое правило: если при вызове некоторого метода в «текущем» классе находится подходящая сигнатура, то компилятор не будет даже смотреть на родительские классы. В данной задаче классы `Bar` и `Baz` имеют собственные версии метода `Quux`. Их сигнатуры подходят под передаваемый набор параметров, а значит они и буду вызваны, а перегруженный `Quux` базового класса будет проигнорирован.

## Ссылки

* Глава [«Overloading»](http://csharpindepth.com/Articles/General/Overloading.aspx) в книге [«C# in Depth»](http://csharpindepth.com/)

[Задача](./OverloadResolutionOverride-P.md)