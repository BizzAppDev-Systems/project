# Copyright (C) 2026: BizzAppDev Systems Pvt. Ltd.(https://www.bizzappdev.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.base.tests.common import BaseCommon


class TestProjectDepartment(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Project = cls.env["project.project"]
        cls.Task = cls.env["project.task"]
        cls.Department = cls.env["hr.department"]
        # Create departments
        cls.department_1 = cls.Department.create(
            {
                "name": "IT Department",
            }
        )
        cls.department_2 = cls.Department.create(
            {
                "name": "HR Department",
            }
        )
        # Create project with department
        cls.project = cls.Project.create(
            {
                "name": "Test Project",
                "department_id": cls.department_1.id,
            }
        )
        # Create task linked to project
        cls.task = cls.Task.create(
            {
                "name": "Test Task",
                "project_id": cls.project.id,
            }
        )

    def test_task_project_department_is_set(self):
        """Task should inherit department from project"""
        self.assertEqual(
            self.task.project_department_id,
            self.department_1,
            "Task project_department_id should match project's department",
        )

    def test_task_project_department_updates_on_project_change(self):
        """Stored related field should update when project department changes"""
        self.project.department_id = self.department_2
        self.assertEqual(
            self.task.project_department_id,
            self.department_2,
            "Task project_department_id should update when project department changes",
        )
