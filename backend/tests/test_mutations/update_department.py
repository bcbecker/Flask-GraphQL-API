update_department_mutation = '''mutation {
  updateDepartment(
    id: "624b4b01150222563a26c128",
    name: "IT/Operations"
  ){
    department{
      id,
      name
    }
  }
}'''