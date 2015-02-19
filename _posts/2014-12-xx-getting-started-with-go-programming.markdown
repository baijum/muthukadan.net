---
layout: post
title: Getting Started with Go Programming
date: 2014-12-xx
categories: golang
---

My last blog post about Go was an introduction to Go programming.  I
hope this post will help you to get start writing Go code.

Firt we will see a quick walk through of the hello world example given
in the introduction.  Then I will exaplain topics like variable,
datatypes, conditions and looping.

This was the hello world example program we used in the introduction:

{% highlight go %}
package main

import "fmt"

func main() {
     fmt.Println("Hello, World!")
}
{% endhighlight %}


The first line declare the name of the package that we are writing.  A
package sources can span multiple files.  If you want to produce an
executable from your program, the name of package should be named as
`main`.  Use all lowercase letters as the package names.

The 3rd line import external packages into the current location.  In
the above example, `fmt` package is imported.  If a package is
imported, it should be used somewhere in the code, otherwise the
compiler will throw error.  If multiple packages need be imported, you
can group the imports into a parenthesized, "factored" import
statement.  Names within the imported package can be referred using a
dot operator as you can see below (`fmt.Println`).  A name is
considered as exported if it begins with a capital letter.  For
example, the name `Foo` is an exported name, but `foo` is not
exported.

The `main` function definition starts with the `func` keyword.  There
should be only one `main` function for an executable program.

Inside the main function, we are calling the `Println` function
available inside the `fmt` package.  the `Println` function prints the
string into standard output and add a new line at the end of the
string.  The curly brace should start in the same line as the function
definition.  Unlike C programming, you don't need to add semi colon at
the end statements.

Now let's looks into topics like variable, datatypes etc.

## Variables

The keyword `var` is used to declare a list of variables.  The
variable declaration can be at package or function level.

{% highlight go %}
var variable type
var variable type = value
var variable = value
var variable1, variable2 type = value1, value2
{% endhighlight %}

If value is not given, a default zero value will be assigned.  The
zero value is: 0 for numeric types, false for boolean type, and empty
string for strings.

Inside a function, the `:=` short assignment statement can be used in
place of a `var` declaration.

These are the basic data types available in Go:

```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```

To convert a value `v` to the type `T`, use the expression: `T(v)`

## For loop

The `for` loop is the only one looping construct available in Go.

Here is an example `for` loop to get sum of values starting from 0
upto 10.

{% highlight go %}
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
{% endhighlight %}

Unlike C programming, there is no paranthesis (()) in the `for` loop.  And
the curly brace ({}) is required, even if there is only one statement.

The initialization and increment part are optional as you can see
below.

{% highlight go %}
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}
{% endhighlight %}

An infinite loop can be created using a `for` without any condition as
given below.

{% highlight go %}
package main

func main() {
	for {
	}
}
{% endhighlight %}

# If

Unlike C programming, there is no paranthesis (()) in the `if`
statement.  And the curly brace ({}) is required, even if there is
only one statement.

{% highlight go %}
package main

import "fmt"

func main() {
	i := 10
	if i < 0 {
		fmt.Println("negative number")
	} else {
		fmt.Println("positive number")
	}
}
{% endhighlight %}


Similar to `for` loop, the `if` statement can start with a short
statement to execute before the condition.  See the example given
below.

{% highlight go %}
package main

import "fmt"

func main() {
	if i := 10; i < 0 {
		fmt.Println("negative number", i)
	} else {
		fmt.Println("positive number", i)
	}
}
{% endhighlight %}

Any variable that is declared along with `if` statement is only
available within the `if` and `else` blocks.

# Switch

A case body breaks automatically, unless it ends with a fallthrough statement.

Switch cases evaluate cases from top to bottom, stopping when a case succeeds.

(For example,

switch i {
case 0:
case f():
}
does not call f if i==0.)

Switch without a condition is the same as switch true.

This construct can be a clean way to write long if-then-else chains.

## Defer

A defer statement defers the execution of a function until the
surrounding function returns.

The deferred call's arguments are evaluated immediately, but the
function call is not executed until the surrounding function returns.

Deferred function calls are pushed onto a stack.  When a function
returns, its deferred calls are executed in last-in-first-out order.
