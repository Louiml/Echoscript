# Echoscript
### EchoScript is a programming language that was created with Python. It has a simple syntax and is designed to make it easy for beginners to learn programming. EchoScript allows users to write code that performs a wide range of tasks, from simple calculations to complex algorithms.

### The code example provided shows how EchoScript can be used to define functions and variables. The code defines two functions, greet and bye, which both output strings to the console. It also defines two variables, name and age, using the addvar keyword.

### The format of the language is `.ecs`, which stands for EchoScript. The code can be run by using the command python `echoscript.py -compile sample.ecs`, where sample.ecs is the name of the file containing the EchoScript code.

### Overall, EchoScript is a user-friendly programming language that can be used to perform a variety of tasks. Its simple syntax makes it a great option for beginners who are just starting to learn programming.

```ecs
funccmd<greet>[
out Hello, EchoScript!
]

funccmd<bye>[
out Goodbye, EchoScript!
]

addvar name =e= John
addvar age =e= 30

greet
bye
out $age$
```
