all_departments_query = '''query{
  allDepartments {
    edges {
      node {
        id,
        name
      }
    }
  }
}'''