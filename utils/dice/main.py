import re
import random
from typing import List

from mojimoji import zen_to_han

# コマンドを分割
def command_splitter (string: str) -> List[str]:
    return sum([re.split('(\-)', _) for _ in re.split('(\+)', string)], [])

# ダイスを振る
def roll_dice (dice: str) -> List[int]:
    articles, faces = re.split('[d]', dice)

    if articles == '0' or faces == '0':
        return [0]
    
    result = [0] * int(articles)
    for i in range(int(articles)):
        result[i] = random.randint(1, int(faces))

    return result

# コマンド実行
def exec_command (command: str) -> str:

    elements = command_splitter(zen_to_han(command))
    result = ''
    total = 0

    is_plus = True

    for i, elem in enumerate(elements):
        if elem == '+':
            result += elem
            is_plus = True

        elif elem == '-':
            result += elem
            is_plus = False

        elif 'd' in elem:
            rolled = roll_dice(elem)

            if rolled == [0]:
                result += '0 '
                continue

            result += f'{sum(rolled)}[{", ".join(map(str, rolled))}]'
            if is_plus:
                total += sum(rolled)
            else:
                total -= sum(rolled)

        else:
            result += elem
            if is_plus:
                total += int(elem)
            else:
                total -= int(elem)

        result += ' '
    
    result = f'({command}) ＞ {result}＞ {str(total)}'

    return result

def main():
    command = input('command >> ').split()[0]
    result = exec_command(command)
    print(result)

if __name__ == '__main__':
    main()
