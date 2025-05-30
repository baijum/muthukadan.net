---
title: Mathematical Equations with MathJax
date: 2025-05-30
category: Mathematics
tags: MathJax, LaTeX, Equations
excerpt: This post demonstrates how to use MathJax to render beautiful mathematical equations in your blog posts.
---

# Mathematical Equations with MathJax

This post demonstrates how to use MathJax to render beautiful mathematical equations in your blog posts. MathJax is a JavaScript display engine that works in all browsers and uses LaTeX syntax for writing equations.

## Inline Equations

You can include inline equations like $E = mc^2$ or $\pi \approx 3.14159$ within your text. Simply surround your LaTeX code with single dollar signs `$...$`.

## Display Equations

For more complex equations or to display them on their own line, use double dollar signs:

$$
\frac{d}{dx}\left( \int_{a}^{x} f(u)\,du\right)=f(x)
$$

This is the Fundamental Theorem of Calculus.

## More Examples

### Quadratic Formula

The solutions to $ax^2 + bx + c = 0$ are given by:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Matrices

You can also display matrices:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

### Calculus

The definition of a derivative:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

### Statistics

The normal distribution probability density function:

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

### Physics

Maxwell's equations in differential form:

$$
\begin{align}
\nabla \cdot \vec{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \vec{B} &= 0 \\
\nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} \\
\nabla \times \vec{B} &= \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
\end{align}
$$

## Using MathJax in Your Posts

To include mathematical equations in your posts, you can use:

1. Inline math with single dollar signs: `$E = mc^2$` renders as $E = mc^2$
2. Display math with double dollar signs: `$$E = mc^2$$` renders as:

$$
E = mc^2
$$

MathJax supports a wide range of LaTeX commands and environments, making it possible to display complex mathematical content on the web.

## Conclusion

With MathJax support, you can now include beautiful mathematical equations in your blog posts, making it perfect for explaining scientific concepts, engineering principles, or mathematical theories.
