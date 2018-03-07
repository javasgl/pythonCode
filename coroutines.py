
import asyncio

async def task(n):
	print("do task:",n)

tasks = [ task(_) for _ in range(10)]

loop = asyncio.get_event_loop()
res, _ = loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# def task_with_coroutine(n):
# 	print("do task:",n)

# for _ in range(10):
# 	task_with_coroutine(_)
