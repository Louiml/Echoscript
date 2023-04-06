import argparse
import os
import sys
import time
import random
import re

class EchoScript:
    def __init__(self):
        self.commands = {
            'out': self.out,
            'funccmd': self.funccmd,
            'addvar': self.addvar,
        }
        self.functions = {}
        self.variables = {}

    def out(self, text):
        var_pattern = r'\$(.*?)\$'
        var_match = re.search(var_pattern, text)
        if var_match:
            var_name = var_match.group(1)
            if var_name in self.variables:
                text = text.replace(f"${var_name}$", self.variables[var_name])
                print(text)
            else:
                raise ValueError(f"\033[31mError: Unknown variable '{var_name}'\033[0m")
        else:
            print(text)

    def funccmd(self, func_name, func_body):
        self.functions[func_name] = func_body

    def addvar(self, name_value):
        name, value = name_value.split(' =e= ')
        self.variables[name] = value

    def call_function(self, func_name):
        if func_name in self.functions:
            self.parse(self.functions[func_name])
        else:
            print(f"\033[31mError: Function '{func_name}' not found\033[0m")

    def parse(self, code):
        lines = iter(code.strip().split('\n'))
        try:
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                funccmd_match = re.match(r'funccmd<(.*?)>', line)
                if funccmd_match:
                    func_name = funccmd_match.group(1)
                    line = next(lines).strip()
                    func_body_lines = []
                    while line != ']':
                        func_body_lines.append(line)
                        line = next(lines).strip()
                        func_body = '\n'.join(func_body_lines)
                        self.commands['funccmd'](func_name, func_body)
                else:
                    tokens = line.split(' ', 1)
                    command, args = tokens[0], tokens[1] if len(tokens) > 1 else ''
                    if command in self.commands:
                        try:
                            self.commands[command](args)
                        except ValueError as e:
                            print(e)
                            return 
                    elif command in self.functions:
                        self.call_function(command)
                    else:
                        print(f"\033[31mError: Unknown command '{command}'\033[0m")
        except StopIteration:
            pass

def read_ecs_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def loading_animation():
    animation = "|/-\\"
    delay_range = (1, 520)

    start_time = time.time()
    duration = random.uniform(*delay_range) 

    while time.time() - start_time < duration:
        for i in range(len(animation)):
            sys.stdout.write("\rLoading " + animation[i % len(animation)])
            sys.stdout.flush()
            time.sleep(0.1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EchoScript Compiler")
    parser.add_argument("-compile", dest="file_name", required=True, help="Name of the .ecs file to compile")
    args = parser.parse_args()

    es = EchoScript()
    ecs_file_path = args.file_name

    if not ecs_file_path.endswith(".ecs"):
        print("\033[41mError: Input file must have a .ecs extension\033[0m")
    else:
        if os.path.exists(ecs_file_path):
            ecs_code = read_ecs_file(ecs_file_path)
            loading_animation()
            print("\n")
            print("\033[42m----------------------------------------\033[0m")
            print("\033[42m|\033[0m")
            es.parse(ecs_code)
            print("\033[42m|\033[0m")
            print("\033[42m----------------------------------------\033[0m")
        else:
            print(f"\033[41mError: File '{ecs_file_path}' not found\033[0m")
