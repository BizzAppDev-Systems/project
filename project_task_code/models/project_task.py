# Copyright 2016 Tecnativa <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

PROJECT_TASK_WRITABLE_FIELDS = {
    "code",
}


class ProjectTask(models.Model):
    _inherit = "project.task"
    _rec_names_search = ["name", "code"]

    code = fields.Char(
        string="Task Number",
        required=True,
        default="/",
        readonly=True,
        copy=False,
    )

    _project_task_unique_code = models.Constraint(
        "UNIQUE (company_id, code)",
        "The code must be unique!",
    )

    @property
    def TASK_PORTAL_WRITABLE_FIELDS(self):
        return super().TASK_PORTAL_WRITABLE_FIELDS | PROJECT_TASK_WRITABLE_FIELDS

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("code", "/") == "/":
                vals["code"] = (
                    self.sudo().env["ir.sequence"].next_by_code("project.task") or "/"
                )
        return super().create(vals_list)

    @api.depends("name", "code")
    def _compute_display_name(self):
        result = super()._compute_display_name()
        for task in self.filtered("code"):
            task.display_name = f"[{task.code}] {task.display_name}"
        return result
