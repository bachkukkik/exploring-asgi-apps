## placeholder for the function definition
async def some_endpint():
    ...


## basic http handler
async def app(scope, receive, send):
    if scope["type"] == "http":
        return
    response = await some_endpint()
    await response(scope, receive, send)

## equivalent class handler
class App:
    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            return
        response = await some_endpint() ## e.g. from starlette.responses import Response
        await response(scope, receive, send)


## class with routes
class App:
    async def __init__(self):
        self.routes = []

    async def mount(self, path, handler):
        self.routes.append((path, handler))

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            return
        response = await some_endpint() ## e.g. from starlette.responses import Response
        await response(scope, receive, send)

app = App()
app.mount("/", some_endpint)