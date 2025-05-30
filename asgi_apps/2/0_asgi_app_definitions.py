async def application(scope, receive, send):
    event = await receive()
    ...
    await send({"type": "websocket.send", ...: ...})

# These events each have a defined type key, which can be used to infer the event’s structure. 
# Here’s an example event that you might receive from receive with the body from a HTTP request:

{
    "type": "http.request",
    "body": b"Hello World",
    "more_body": False,
}

# And here’s an example of an event you might pass to send to send an outgoing WebSocket message:

{
    "type": "websocket.send",
    "text": "Hello world!",
}