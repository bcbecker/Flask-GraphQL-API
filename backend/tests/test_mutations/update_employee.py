update_employee_mutation = '''mutation {
  updateEmployee(
    id: "624b4956150222563a26c127",
    name: "Steve"
    tasks:["Code"] 
  ){
    employee{
      id,
      name,
      tasks{
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