from starlette.types import Scope, Message, Receive, Send
import re

total_connections = 0

async def handler_lifspan(scope: Scope, receive: Receive, send: Send) -> None:
    assert scope["type"] == "lifespan"
    while True:
        event = await receive()
        # ## need to handle the event type
        # print(f"Received event: {event}")

        ## handle the event type
        if event["type"] == "lifespan.startup":
            await send({"type": "lifespan.startup.complete"})
        elif event["type"] == "lifespan.shutdown":
            await send({"type": "lifespan.shutdown.complete"})
            break

async def echo_endpoint(scope: Scope, receive: Receive, send: Send):
    ...

async def status_endpoint(scope: Scope, receive: Receive, send: Send):
    ...

async def read_item(scope: Scope, receive: Receive, send: Send, item_id: str):
    ...

async def error_endpoint(scope: Scope, receive: Receive, send: Send):
    ...

async def handler_http(scope: Scope, receive: Receive, send: Send):
    assert scope["type"] == "http"
    if scope["path"] == "/echo" and scope["method"] == "POST":
        await echo_endpoint(scope, receive, send)
    elif scope["path"] == "/status" and scope["method"] == "GET":
        await status_endpoint(scope, receive, send)
    elif (m := re.match("/item/(\w+)", scope["path"])) and scope["method"] == "GET":
        await read_item(scope, receive, send, item_id=m.group(1))
    else:
        await error_endpoint(scope, receive, send)

async def app(scope: Scope, receive: Receive, send: Send) -> None:
    global total_connections
    total_connections += 1
    current_connection = total_connections
    
    print(f"Begin connection {current_connection}.")

    if scope["type"] == "lifespan":
        await handler_lifspan(scope, receive, send)
    elif scope["type"] == "http":
        await handler_http(scope, receive, send)
    # elif scope["type"] == "websocket":
    #     await handler_websocket(scope, receive, send)
    
    print(f"End connection {current_connection}")

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info", use_colors=False)

if __name__ == "__main__":
    main()