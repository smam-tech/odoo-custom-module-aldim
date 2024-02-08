from odoo import models, fields, api, http
from odoo.http import request, content_disposition, Response
import xlsxwriter
import io
from datetime import datetime


class SMAMMaterialExcelReportController(http.Controller):
    @http.route([
        '/smam_material/excel_report/<model("smam.material"):report_id>',
    ], type='http', auth="user", csrf=False)
    def get_sale_excel_report(self, report_id=None, **args):

        # VARIABLE INITIATION 
        export_excel_location = "report.xlsx"
        response = request.make_response(
            None,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition(export_excel_location))
            ]
        )

        #Init excel in tmp
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet("Report Material")

        worksheet.write('A1', report_id.smam_material_code)
        worksheet.write('B1', report_id.smam_name)
        worksheet.write('C1', report_id.smam_type)
        worksheet.write('D1', report_id.smam_buy_price)
        worksheet.write('E1', report_id.smam_supplier.name)

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
        return response