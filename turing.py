# ---------------------------------------------------------------------------
# Implémentation d'une machine de Turing
# ---------------------------------------------------------------------------
# Auteur : Steph (https://github.com/steph-d3v/)
# Date   : 14 octobre 2024
# ---------------------------------------------------------------------------
# fmt: off

from sys import argv
from time import sleep

Tape = list[str]
Program = dict[tuple[str, str], tuple[str, str, str]]

def show(state: str, tape: Tape, head: int, delay: float, last: bool = False):
    print(f"\r{(s := ''.join(tape))[:head]}\033[37;1m{s[head]}\033[0m{s[head+1:]} [{state}]", end="\n" if last else "")
    sleep(delay)

def main(source: str, input_tape: str, states: str, input_head: str):
    tape: Tape = list(input_tape)
    head = int(input_head)
    state, stops = (s := states.split(":"))[0], s[1].split(",")
    program: Program = {}
    for line in [source[i:i+5] for i in range(0, len(source), 5)]:
        s, r, w, m, n = line  # state, read, write, move, new state
        program[s, r] = (w, m, n)
    show(state, tape, head, 1, halt := state in stops)
    while not halt:
        w, m, n = program[s := state, r := tape[head]]
        tape[head] = w if w != " " else r
        head += -1 if m == "<" else 1 if m == ">" else 0
        state = n if n != " " else s
        show(state, tape, head, 0.05, halt := state in stops)

if __name__ == "__main__":
    main(*argv[1:])
