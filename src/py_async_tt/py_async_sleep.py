from asyncio import sleep
import asyncio
import time


class AsyncSleep:
    async def read_byte(self, message: str) -> bytes:
        await sleep(0.01)
        return message.encode(encoding="utf-8")

    async def read(self) -> tuple:
        try:
            start = time.time()
            async with asyncio.TaskGroup() as tg:
                task1 = tg.create_task(self.read_byte("a"))
                task2 = tg.create_task(self.read_byte("b"))
                task3 = tg.create_task(self.read_byte("c"))
            results = [task1.result(), task2.result(), task3.result()]
            results_byte = results[0] + results[1] + results[2]
            elapsed_time = time.time() - start
            print(f"{elapsed_time=:.3f}[sec]")
            return results_byte, elapsed_time
        except* ValueError as err:
            print(f"{err.exceptions=}")
        except* TypeError as err:
            print(f"{err.exceptions=}")
