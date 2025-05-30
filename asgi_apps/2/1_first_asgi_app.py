from pprint import pprint

## easy way
from starlette.types import Scope, Message, Receive, Send

# ## hard way
# from typing import Any, Callable, Awaitable, MutableMapping
# type Scope = MutableMapping[str, Any]
# type Message = MutableMapping[str, Any]
# type Receive = Callable[[], Awaitable[Message]]
# type Send = Callable[[Message], Awaitable[None]]

total_connections = 0

async def app(scope: Scope, receive: Receive, send: Send) -> None:
    global total_connections
    total_connections += 1
    current_connection = total_connections
    
    pprint(f"Begin connection {current_connection}.")
    pprint("Scope:")
    pprint(scope)
    pprint(f"End connection {current_connection}")

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info", use_colors=False)

if __name__ == "__main__":
    main()