class MyContextManager:
    def __init__(self):
        print("MyContextManager int", id(self))
        def __enter__(self):
            print("Entering 'with' context")
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"{exc_type=} {exc_val=} {exc_tb=}")
            print("Exiting 'with' context")
            return True