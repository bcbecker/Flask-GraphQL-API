employee_query = '''query {
  employee(name: "Roy"){
    id,
    name,
    hiredOn,
    department {
          id,
          name
        },
    manager {
      id,
      name
    }
  }
}'''