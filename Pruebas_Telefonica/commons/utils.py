# -*- coding: utf-8 -*-

import json


def generalProperties():
    with open("../resource/properties.json") as confiProp:
        generalProperties = json.load(confiProp)

    return generalProperties
