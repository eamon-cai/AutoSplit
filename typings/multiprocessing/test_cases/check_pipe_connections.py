from __future__ import annotations

from multiprocessing.connection import Pipe, PipeConnection

# Less type-safe, but no extra variable. User could mix up send and recv types.
a: PipeConnection[str, int]
b: PipeConnection[int, str]
a, b = Pipe()

# More type safe, but extra variable
connections_wrong: tuple[
    PipeConnection[str, int], PipeConnection[str, int],
] = Pipe()  # pyright: ignore[reportGeneralTypeIssues]
connections_ok: tuple[PipeConnection[str, int], PipeConnection[int, str]] = Pipe()
a, b = connections_ok

a.send("test")
a.send(0)  # pyright: ignore[reportGeneralTypeIssues]
test: str = b.recv()
test2: int = b.recv()  # pyright: ignore[reportGeneralTypeIssues]

b.send("test")  # pyright: ignore[reportGeneralTypeIssues]
b.send(0)
test: str = a.recv()  # pyright: ignore[reportGeneralTypeIssues]
test2: int = a.recv()