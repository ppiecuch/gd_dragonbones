def can_build(env, platform):
    return platform != "android" or env["android_rtti"]


def configure(env):
    pass
