# coding: utf-8

import os
from test.test_catalog import TestCatalogBase, BASE_PATH


class TestCatalogLayerGroup(TestCatalogBase):

    def test_getlayergroups(self):
        # ws = self.catalog.get_default_workspace()
        layersgroups = self.catalog.get_layergroups()
        print("Layergroups: {}".format(layersgroups))
