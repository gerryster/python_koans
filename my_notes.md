# Ryan's Python Notes and Questions

Use `sniffer` in the python3 directory to automatically run the tests.

## Questions

### Strings

Q: What is with the triple quoted strings?

A: They allow for multiline strings and do require less quoting of internal quotes.

## Notes

* https://github.com/hhatto/autopep8 is used for auto code formatting (at least according to VS Code's plugin recommendations).
  * https://github.com/ruby-formatter/rufo seems to be a similar Ruby idea.

* Python Tutorial: https://docs.python.org/3/tutorial/index.html

* Functions like list and range are built in global functions [documented here](https://docs.python.org/3/library/functions.html)

* There is an "is" operator to test for type equality: `None is None`

### Documentation

When doing Google searches, filtering to the official documentation is essential. Append this to queries:

site:https://docs.python.org/

Python has reached the point in the hype cycle where there is advertising revenue for creating sub-par content which needs to be filtered out.

### Culture

See `import this`. "There should be one-- and preferably only one --obvious way to do it." Opposite of Perl's there is more than one way to do it.

# Basic Types

Null is referred to as "None"

True and False are capitalized.

### Regular Expressions

Provided by the [re|https://docs.python.org/3/library/re.html] module. Regular expression literals are defined using the "r" operator which avoids backslashitus. So, matching 'a', followed by whitespace, followed by 'b', would be accomplished with:

```python
import re
re.search(r'a\s+b', 'a  b')
```

The "r" strings are referred to as "raw strings" can can be used anywhere, even outside of Regular expressions. They are similar to single quoted strings in Ruby.

### Methods

* Access control (private methods) are not a thing.
  * Underscore prefixes are used.
  * Double underscore renames the method with the class name. However, this is done to avoid subclass collisions instead of access control.
* Methods which doe not take a self parameter are global.
* Varargs is supported with a star before the argument like in Ruby.
* Default parameter values are a thing.
