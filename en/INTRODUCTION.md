# Introduction

This book is a collection of problems on the knowledge of the .NET platform and the C# programming language. 
To avoid misunderstandings, just want to say that the book *is not*:

* This book is not a universal way to check your knowledge platform .NET. If you are easily solved all problems, it does not mean that you is a wonderful .NET-programmer. And if you met a lot of new things for yourself, then it does not mean that you don't know .NET.
* This book is not a compilation of new, previously unseen problems. Many examples can be found in the literature, in questions on [StackOverflow](http://stackoverflow.com/), in programmer's blogs. Just because they have become classics.
* This book is not focused on those who already feel Senior .NET Developer and want to learn a lot.

So what is this book? ProblemBook.NET is an attempt to gather in one place a variety of interesting practical problems on the knowledge platform. Problems are divided into chapters, so you can not read everything, but only questions of those areas that are of interest to you. In this book you will not find a deep philosophical questions such as "What is a class?" or "Why is polymorphism needed?". Most of the problems is a piece of C#-code for which you should to determine the result. Each question is provided with a solution (sometimes with a description of why .NET behaves this way).

It is recommended to treat the problem is not as a way to test your knowledge as well as the starting point for the discussion of various aspects of the platform. If you find something new for yourself, it's a great cause to learn .NET a little more detail. Try to play around with the code: modify it and learn how changes affect the result. Read the relevant literature. Think about how the new knowledge can be useful to you in your work.

ProblemBook.NET distributed electronically, the development is on GitHub. It should also be noted that at present the problem book is far from the final version. The book will be updated with new problems and old will be refined and improved.

## Technical Details
Today, there are two popular platform implementation .NET: The original Microsoft .NET Framework (hereinafter - MS.NET) and Mono. It is known that the behavior of some code fragments may change when you change the implementation. Similarly, the behavior might depends on the CLR or processor architecture. If the result of the fragment of the code depends on the environment, it is likely that the answers will be given an explanation. However, it is *not guaranteed*. If one of the examples you have received an answer that is different from this in the book, please contact the author, that he corrected this mistake.

Examples of code in all tasks can be run from [LINQPad](http://www.linqpad.net/) (in C# Statements or C# Program, depending on the availability of the method `Main`), but you should import the following namespace (Query -> Query Properties -> Additional Namespace Imports):

```
System.Globalization
System.Runtime.InteropServices
System.Runtime.CompilerServices
```

## Thanks
The author sincerely thanks the Chief Editor Ivan Pashchenko for useful discussions during the writing of this book.

The author evinces appreciation to Ekaterina Demidova for the kindly providing illustrations.