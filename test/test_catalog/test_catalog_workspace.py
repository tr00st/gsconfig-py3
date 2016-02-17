# coding: utf-8


from test.test_catalog import TestCatalogBase


class TestCatalogWorkspace(TestCatalogBase):

    def tearDown(self):
        super(TestCatalogWorkspace, self).tearDown()
        try:
            ws = self.catalog.get_workspace("gsconfig_test_create_workspace")
            self.catalog.delete(ws)
        except:
            pass

    def test_default_workspace(self):
        current = self.catalog.get_default_workspace()
        self.catalog.set_default_workspace(self.workspace.name)
        new = self.catalog.get_default_workspace()
        self.assertEqual(new.name, self.workspace.name)
        self.catalog.set_default_workspace(current.name)

    def test_create_workspace(self):
        old_ws = self.catalog.get_workspaces()
        ws = self.catalog.create_workspace("gsconfig_test_create_workspace")
        new_ws = self.catalog.get_workspaces()
        self.assertEqual(ws.name, "gsconfig_test_create_workspace")
        self.assertEqual(len(old_ws) + 1, len(new_ws))
