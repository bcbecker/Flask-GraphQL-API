delete_employee_mutation = '''mutation {
  deleteEmployee(
    id: "624b4956150222563a26c127"
  ){
    employee{
      id,
      name
    }
  }
}'''