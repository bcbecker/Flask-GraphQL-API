update_role_mutation = '''mutation {
  updateRole(
    id: "624b4e95150222563a26c129"
    name: "qa tester"
  ){
    role{
      id,
      name
    }
  }
}'''