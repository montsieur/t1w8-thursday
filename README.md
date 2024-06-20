# T1w8 Thursday

# 4 Pillars of OOP
- Banking System

# __repr__ method
- Special method, like __init__ which is used to define a string representation for an object.
- Particularly used for debugging and development because it can give detaILED info about an object

# Composition of OOP
- Design principle where a class is composed of one or more objects from other classes.
- It's an alternative to inheritance and is often more flexible and modular.
- Avoids inheritance's pitfall: Changes in base class can unintentionally affect the derived class, which may break their functionality.
- Composition does not directly affect the composed class, as the class inherits with component classes through well-defined interfaces.

# Error Handling
## Taxnomy of python Errors
- Silent Logical Errors - Code that run fine, but are logically incorrect
- Assertion Errors - Raised when 'assert' statement fails. If condition is True, nothing happens, if false, raises Assertion error.
- Syntax Errors - Errors in the written syntax, that Python interpreter cannot understand. 
- Exceptions - Runtime errors, occurs during program execution. Python has built-in exception to handle common errors.

# Stack Trace Interpretation
- Text that appears when Python encounters an exception, "stack trace"
- When exception occurs, the interpreter prints a stack trace that shows where the error happened and how the code reached that point.
- Start with: Exception, then the trace.

# Try / Except / Finally
- Comprehensive way to handle exceptions
- Ensures the code always runs, regardless whether an error occurs or not.
- 'try' block has code that may raise exception
- 'except' block has code that handles the exception
- 'finally' block has the code that should always be executed
