all_roles_query = '''query{
  allRoles {
    edges {
      node {
        id,
        name
      }
    }
  }
}'''