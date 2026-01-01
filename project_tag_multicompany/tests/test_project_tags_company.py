# Copyright (C) 2026: BizzAppDev Systems Pvt. Ltd.(https://www.bizzappdev.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.addons.base.tests.common import BaseCommon


class TestProjectTagsCompany(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ProjectTags = cls.env["project.tags"]
        cls.company = cls.env.company
        cls.tag = cls.ProjectTags.create(
            {
                "name": "Test Tag",
                "company_id": cls.company.id,
            }
        )

    def test_company_id_exists(self):
        """Ensure company_id can be assigned and stored"""
        self.assertEqual(
            self.tag.company_id,
            self.company,
            "company_id should be correctly set on project tag",
        )
