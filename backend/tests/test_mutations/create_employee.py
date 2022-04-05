create_employee_mutation = '''mutation {
  createEmployee(
    name: "Kevin", 
		departmentId: "624497d14fdd177670ec98ff",
		rolesId: ["624497d14fdd177670ec9902"],
		managerId: "624497d14fdd177670ec9903"
  ){
    employee{
      id,
      name,
      hiredOn,
      department {
          id,
          name
        },
        roles {
          edges {
            node {
              id,
              name
            }
          }
        },
        manager {
          id,
          name
        }
        tasks {
          edges {
            node {
              name,
              deadline
            }
          }
        }
    	}
    }
  }'''