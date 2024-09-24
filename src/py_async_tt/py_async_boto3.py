import asyncio
from io import BytesIO
import time
import aioboto3


class AsyncBoto3:
    async def read_byte(self, bucket_name: str, key: str) -> bytes:
        session = aioboto3.Session()
        async with session.client("s3") as s3:
            b = BytesIO()
            start = time.time()
            await s3.download_fileobj(bucket_name, key, b)
            elapsed_time = time.time() - start
            print(f"download elapsed_time: {(elapsed_time):.3f}[sec]")
            return b.getvalue()

    async def read(self) -> tuple:
        try:
            start = time.time()
            async with asyncio.TaskGroup() as tg:
                task1 = tg.create_task(self.read_byte("ma2moto-bucket", "test.json"))
                task2 = tg.create_task(self.read_byte("ma2moto-bucket", "test.json"))
                task3 = tg.create_task(self.read_byte("ma2moto-bucket", "test.json"))
            results = [task1.result(), task2.result(), task3.result()]
            results_byte = results[0] + results[1] + results[2]
            elapsed_time = time.time() - start
            print(f"{elapsed_time=:.3f}[sec]")
            return results_byte, elapsed_time
        except* ValueError as err:
            print(f"{err.exceptions=}")
        except* TypeError as err:
            print(f"{err.exceptions=}")
