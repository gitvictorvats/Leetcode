# Write your MySQL query statement below

select unique_id,name 
from Employees
Left Join EmployeeUNI
On Employees.id=EmployeeUNI.id
