class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event_name, handler):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(handler)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self._events:
            for handler in self._events[event_name]:
                handler(*args, **kwargs)


# 使用示例
event_emitter = EventEmitter()

# 定义事件处理函数
def event_handler(message):
    print(f"Received event: {message}")

# 订阅事件
event_emitter.on('event1', event_handler)

# 发布事件
event_emitter.emit('event1', 'Hello, world!')

def add(x, y):
    return x+y
def apply_async(func, args, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

mylog = 'Hello, world!'
apply_async(add, ('hello', 'world'), callback=lambda result: event_emitter.emit('event1', result))

apply_async(event_handler, ('h'), event_emitter.emit)
