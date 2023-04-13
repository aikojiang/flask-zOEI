from steamship import Steamship

# TODO: Replace with your package and instance handle below
instance = Steamship.use("PACKAGE_HANDLE", "INSTANCE_HANDLE", config={
    "default_name": "Beautiful"
})

print(instance.invoke("greet"))
