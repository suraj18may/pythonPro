from openpyxl import *
wb=Workbook()
ws=wb.active

testdata=[['Name','EmpId','salary','city',],['Mrinal',101,80000,"Noida"],['Mohit',102,60000,"Gurgaon"],['Manish',103,70000,"Pune"]]
for data in testdata:
    ws.append(data)
wb.save("employee.xlsx")