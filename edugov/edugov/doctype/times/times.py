# Copyright (c) 2024, AlphaCode and contributors
# For license information, please see license.txt

# # import frappe
# from frappe.model.document import Document
# from datetime import datetime

# class Times(Document):
#     def autoname(self):
#         if self.start_time and self.end_time:
#             try:
#                 # إذا كانت القيم من نوع نص، قم بتحويلها إلى كائنات وقت
#                 start_time = datetime.strptime(self.start_time, "%H:%M:%S").time() if isinstance(self.start_time, str) else self.start_time
#                 end_time = datetime.strptime(self.end_time, "%H:%M:%S").time() if isinstance(self.end_time, str) else self.end_time

#                 # صياغة الوقت بتنسيق HHMMSS
#                 start_time_formatted = start_time.strftime("%H%M%S")
#                 end_time_formatted = end_time.strftime("%H%M%S")

#                 # تعيين الاسم باستخدام التوقيت المخصص
#                 self.name = f"{start_time_formatted}-{end_time_formatted}"
#             except ValueError:
#                 # التعامل مع الخطأ في حال كان التنسيق غير صحيح
#                 frappe.throw("تنسيق الوقت غير صحيح. يرجى إدخال الوقت بتنسيق HH:MM:SS.")
#         else:
#             # اسم بديل في حال عدم إدخال الأوقات
#             self.name = frappe.generate_hash(length=8)

from frappe.model.document import Document
from datetime import datetime

class Times(Document):
    def autoname(self):
        if self.start_time and self.end_time:
            try:
                # تحويل start_time و end_time إلى كائنات وقت إذا كانت مخزنة كنصوص
                end_time = datetime.strptime(self.end_time, "%H:%M:%S").time() if isinstance(self.end_time, str) else self.end_time

                start_time = datetime.strptime(self.start_time, "%H:%M:%S").time() if isinstance(self.start_time, str) else self.start_time

                # صياغة الوقت بتنسيق HH:MM:SS مع النقطتين
                end_time_formatted = end_time.strftime("%H:%M:%S")
                start_time_formatted = start_time.strftime("%H:%M:%S")
               

                # تعيين الاسم باستخدام الأوقات المخصصة
                self.name = f"{start_time_formatted}-{end_time_formatted}"
            except ValueError:
                # التعامل مع الخطأ في حال كان التنسيق غير صحيح
                frappe.throw("تنسيق الوقت غير صحيح. يرجى إدخال الوقت بتنسيق HH:MM:SS.")
        else:
            # اسم بديل في حال عدم إدخال الأوقات
            self.name = frappe.generate_hash(length=8)


