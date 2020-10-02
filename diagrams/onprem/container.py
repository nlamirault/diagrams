# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Container(_OnPrem):
    _type = "container"
    _icon_dir = "resources/onprem/container"


class Containerd(_Container):
    _icon = "containerd.png"


class Crio(_Container):
    _icon = "crio.png"


class Docker(_Container):
    _icon = "docker.png"


class Gvisor(_Container):
    _icon = "gvisor.png"


class Rkt(_Container):
    _icon = "rkt.png"


# Aliases

RKT = Rkt
