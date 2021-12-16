
def can_build(env, platform):
    return (
        not env["production"]
        and (platform != "android" or env["android_rtti"])
        and (platform != "iphone" or env["ios_exceptions"])
    )


def configure(env):
    pass
