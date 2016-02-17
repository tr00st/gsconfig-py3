# coding: utf-8

import os
from test.test_catalog import TestCatalogBase, BASE_PATH


class TestCatalogLayer(TestCatalogBase):

    def test_get_layers(self):
        layers = self.catalog.get_layers()

    def test_layer(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        layer = self.catalog.get_layer("gsconfig_test_create_imagemosaic")
        self.assertEqual(layer.name, "gsconfig_test_create_imagemosaic")
