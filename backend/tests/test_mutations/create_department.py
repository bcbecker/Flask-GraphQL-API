create_department_mutation = '''mutation {
  createDepartment(
    name: "IT Operations"
  ){
    department{
      id,
      name
    }
  }
}'''