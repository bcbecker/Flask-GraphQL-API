create_role_mutation = '''mutation {
  createRole(
    name: "tester"
  ){
    role{
      id,
      name
    }
  }
}'''