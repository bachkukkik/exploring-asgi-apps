from starlette.types import Scope, Message, Receive, Send

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

async def handler_http(scope: Scope, receive: Receive, send: Send):
    assert scope["type"] == "http"
    print("Scope:")
    print(scope)
    while True:
        print("waiting for event")
        event = await receive()
        ## need to handle the event type
        print(f"Received event: {event}")

        ## handle the event type
        if event["type"] == "http.disconnect":
            return
        
        if not event["more_body"]:
            break
        
    response_message = {
        "type": "http.response.start",
        "status": 200,
        "headers": [
            (b"Content-Type", b"text/plain"),
        ],
    }
    print("sending response", response_message)
    await send(response_message)
    response_message = {
        "type": "http.response.body",
        "body": b"Hello World",
        "more_body": False,
    }
    print("sending body", response_message)
    await send(response_message)


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

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info", use_colors=False)

if __name__ == "__main__":
    main()