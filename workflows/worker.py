from stevedore import driver

def main():
    args = ()
    kwargs = {}
    plugin_namespace="workflows.plugins"
    name = "testflow"

    mgr = driver.DriverManager(
        namespace=plugin_namespace,
        name=name,
        invoke_on_load=True,
        invoke_args=args,
        invoke_kwds=kwargs)

    data = {"a":"b"}
    output = mgr.driver.run(data=data)
    print output
