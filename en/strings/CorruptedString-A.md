# “CorruptedString” (Solution)
You can use the internment mechanism:
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
[Problem](./CorruptedString-Q.md)
