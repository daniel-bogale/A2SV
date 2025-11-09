# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        catalog = {
            employee.id: employee for employee in employees
        }

        def getImp(id: int) -> int:
            employee = catalog[id]
            imp = employee.importance

            for subordinate_id in employee.subordinates:
                imp += getImp(subordinate_id)
            return imp
        
        return getImp(id)