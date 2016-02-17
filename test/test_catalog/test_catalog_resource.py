# coding: utf-8

import os
from test.test_catalog import TestCatalogBase, BASE_PATH


class TestCatalogResource(TestCatalogBase):

    def test_get_resources(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        resources = self.catalog.get_resources()
        print("Resources: {}".format(resources))

    def test_get_resource(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        resource_name = "gsconfig_test_create_imagemosaic"
        resource = self.catalog.get_resource(resource_name, store=ds)
        print("Resource: {}".format(resource))
