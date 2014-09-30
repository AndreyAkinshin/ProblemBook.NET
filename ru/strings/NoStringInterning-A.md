# «NoStringInterning» (Решение)

Нет. Документация [гласит](http://msdn.microsoft.com/en-us/library/system.runtime.compilerservices.compilationrelaxations.aspx), что в этом `NoStringInterning` лишь помечает сборку, как не требующую интернирования. Поэтому CLR только может не интернировать строки, но не обязана. Кроме того, мы всегда может заинтернировать строку через метод `String.Intern`.

[Задача](./NoStringInterning-Q.md)