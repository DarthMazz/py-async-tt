import pytest
from py_async_tt.py_async_boto3 import AsyncBoto3
from py_async_tt.py_async_sleep import AsyncSleep


class TestAsyncTt:

    @pytest.mark.asyncio
    async def test_async_io(self):
        io_module = AsyncSleep()
        res, proc_time = await io_module.read()
        assert res == "abc".encode(encoding="utf-8")

    @pytest.mark.asyncio
    async def test_async_boto3(self):
        io_module = AsyncBoto3()
        res, proc_time = await io_module.read()
