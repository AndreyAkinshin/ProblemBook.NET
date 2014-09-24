# «CorruptedString» (Решение)
Можно заинтергировать строку `"Hello"`, а затем через unsafe-код добраться до соответствующего участка памяти и изменить целевое значение:
```cs
var s = "Hello";
string.Intern(s);
unsafe
{
  fixed (char* c = s)
    for (int i = 0; i < s.Length; i++)
      c[i] = 'a';
}
Console.WriteLine("Hello"); // Displays: "aaaaa"
```
[Задача](./CorruptedString-Q.md)
