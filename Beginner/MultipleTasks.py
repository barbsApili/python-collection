import asyncio

## A function the prints out Before, and After
async def Sequence(task_name):
    print(f'Before {task_name}')
    await asyncio.sleep(0.1)
    print(f'After {task_name}')

## Create the event loop
loop = asyncio.new_event_loop()
# Equivalent to get_event_loop
asyncio.set_event_loop(loop)

## A function the starts the the tasks
async def TaskCreator():
    tasks = []
    for task in range(3):
        tasks.append(asyncio.create_task(Sequence(task)))
    await asyncio.wait(tasks)

loop.run_until_complete(TaskCreator())
loop.close()